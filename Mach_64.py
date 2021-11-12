# coding=utf-8
import os
import struct
from Mach import Mach


class Mach_64(Mach):

    def __init__(self):
        self.magicNumber = '64-Bit'

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
                value = struct.unpack(
                    '<' + str(cmdsize - 8) + 's',
                    f.read(cmdsize-8)
                )
                # print(self.loadCommand(cmd))
                # print(value[0].hex().upper())
                type = self.loadCommand(cmd)
                if type == 'LC_UUID':
                    self.uuid = value[0].hex().upper()
                elif type == 'LC_SYMTAB':
                    print(type)
                    print(value)




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