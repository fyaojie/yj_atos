# coding=utf-8
from ctypes import sizeof
import os
import struct
from Mach import Mach
from Section64 import Section64
from SegmentCommand64 import SegmentCommand64
from Symbol import Symbol
from Symtab import Symtab


class Mach_64(Mach):

    def __init__(self):
        self.magicNumber = '64-Bit'

    # 符号表解析
    def analyticalSymbol(self, f):
        f.seek(self.symtab.symoff)

        for i in range(self.symtab.nsyms):
            value = struct.unpack(
                        '<IBBHQ',
                        f.read(16)
                    )
            # print(i)

            currentBol = Symbol(
                value[0],
                value[1],
                value[2],
                value[3],
                value[4]
            )
            # break
            self.symbols.append(currentBol)


        # 这里有很多情况出现符号表索引顺序不正确,进行一次排序校对
        self.symbols.sort(key= lambda x:x.n_strx)

        for i in range(len(self.symbols) - 1):

            currentBol = self.symbols[i]
            nextBol = self.symbols[i + 1]
            currentBol.setNextStrx(nextBol.n_strx)


        # for bol in self.symbols:
        #     print(bol.description())

        # print(len(self.symbols))
        for bol in self.symbols:
            f.seek(self.symtab.stroff + bol.n_strx)
            if bol.lenth > 0:
                value = struct.unpack(
                        '<' + str(bol.lenth) + 's',
                        f.read(bol.lenth)
                    )
                print(value)
            else:
                print('cool')

    def analyticalLine(self, section, f):
        if ('line' in str(section.sectname)) == False:
            return

        size = min(
            section.size,
            20
        )
        f.seek(section.addr + section.offset)
        # value = struct.unpack(
        #             '<' + str(size) + 'c',
        #             f.read(size)
        #         )
        print('test')
        print(section.size)
        print(f.read(section.size))

    def analyticalData(self):
        with open(self.path, 'rb') as f:
            data = f.read(32)
            (magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags, reserved) = struct.unpack(
                '<IiiIIIII',
                data
            )

            self.arch = self.getMachine(cputype)
            self.filetype = self.getFiletype(filetype)

            # print(magic)
            # print(cputype)
            # print(self.arch)
            # print(cpusubtype)
            # print(self.filetype)
            # print(ncmds)
            # print(sizeofcmds)
            # print(flags)
            # print(reserved)
            load_command = '<II'

            for index in range(ncmds):
                (cmd, cmdsize) = struct.unpack(
                    '<II',
                    f.read(8)
                )

                # print(cmd)
                # print(cmdsize)

                # print(self.loadCommand(cmd))
                # print(value[0].hex().upper())
                type = self.loadCommand(cmd)
                if type == 'LC_UUID':
                    value = struct.unpack(
                        '<' + str(cmdsize - 8) + 's',
                        f.read(cmdsize-8)
                    )
                    self.uuid = value[0].hex().upper()
                elif type == 'LC_SYMTAB':

                    self.symtab.cmd = cmd
                    self.symtab.cmdsize = cmdsize

                    (symoff, nsyms, stroff, strsize) = struct.unpack(
                        '<IIII',
                        f.read(16)
                    )
                    self.symtab.symoff = symoff
                    self.symtab.nsyms = nsyms
                    self.symtab.stroff = stroff
                    self.symtab.strsize = strsize
                elif type == 'LC_SEGMENT_64':
                    value = struct.unpack(
                            '<16sQQQQiiII',
                            f.read(64)
                        )
                    print(value)
                    segment = SegmentCommand64()
                    self.segments.append(segment)

                    segment.cmd = cmd
                    segment.cmdsize = cmdsize
                    segment.segname = value[0]
                    segment.vmaddr = value[1]
                    segment.vmsize = value[2]
                    segment.fileoff = value[3]
                    segment.filesize = value[4]
                    segment.maxprot = value[5]
                    segment.initprot = value[6]
                    segment.nsects = value[7]
                    segment.flags = value[8]

                    tempArray = []
                    for index in range(int((cmdsize - 64) / 80)):
                        sectionValue =  struct.unpack(
                                            '<16s16sQQIIIIIIII',
                                            f.read(80)
                                        )

                        tempArray.append(Section64(sectionValue))

                    segment.sections = tempArray
                        # print(sectionValue)

                else:
                    f.seek(cmdsize - 8, 1)
                    print(cmd)
                    print(cmdsize)
                    # value = struct.unpack(
                    #     '<' + str(cmdsize - 8) + 'c',
                    #     f.read(cmdsize-8)
                    # )
                    # print(value)

            # 符号表解析
            # self.analyticalSymbol(f)

            # Section 解析
            for obj in self.segments:
                for tempSection in obj.sections:
                    # print(tempSection.sectname)
                    self.analyticalLine(tempSection, f)

                # break
            # f.seek(self.symtab.stroff)
            # value = struct.unpack(
            #             '<' + str(self.symtab.strsize) + 's',
            #             f.read(self.symtab.strsize)
            #         )
            # print(value[0].hex().upper())
            # self.uuid = value[0].hex().upper()

            # (cmd, cmdsize) = struct.unpack(
            #     '<II',
            #     f.read(8)
            # )
            # # print(cmd)
            # # print(cmdsize)
            # value = struct.unpack(
            #     '<' + str(cmdsize - 8) + 's',
            #     f.read(cmdsize-8)
            # )
            # print(value)


if __name__ == '__main__':
    mach = Mach_64()
    mach.path = os.path.abspath('CMSTest')
    mach.analyticalData()
    print(mach.description())

    # data_path = os.path.abspath('CMSTest')
    # # 读取二进制文件
    # print(data_path)

# # 这里使用小端模式读取
# with open(data_path, 'rb') as f:
#     data = f.read(4)
#     unpacked = struct.unpack(
#         '<I',
#         data
#     )
#     print(unpacked[0])

#     # 读取指针回退
#     f.seek(0)
#     print(0x1000007)
#     #define MH_MAGIC_64 0xfeedfacf /* the 64-bit mach magic number */
#     #define MH_CIGAM_64 0xcffaedfe /* NXSwapInt(MH_MAGIC_64) */
#     MH_MAGIC_64 = 0xfeedfacf
#     MH_CIGAM_64 = 0xcffaedfe

#     if unpacked[0] == 0xfeedfacf or unpacked[0] == 0xfeedfacf:
#         # mach_header 64
#         data1 = f.read(32)
#         (magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags, reserved) = struct.unpack(
#             '<IiiIIIII',
#             data1
#         )
#         print(magic)
