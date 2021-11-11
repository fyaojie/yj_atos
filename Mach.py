# coding=utf-8
from os import nice, path

class Mach:
    path = ''

    # mach-o 位数
    magicNumber = ''
    # def magicNumber(self):
    #     return ''

    # cpu 架构
    arch = ''
    # def arch(self):
    #     return ''

    # 工具版本
    toolVersion = '0.0.1'
    # def toolVersion(self):
    #     return '0.0.1'

    # 符号数量
    symbolsCount = ''
    # def symbolsCount(self):
    #     return ''
    # 文件版本
    fileVersion = ''
    # def fileVersion(self):
    #     return ''
    # UUID
    uuid = ''
    # def uuid(self):
    #     return ''

    # 编译时间
    buildTime = ''
    # def buildTime(self):
    #     return ''

    # 符号表
    symbolTable = ''
    # def symbolTable(self):
    #     return ''

    # 文件类型
    filetype = ''

    def description(self):
        return  'File: ' + self.path + '\n' + \
                'Format: ' + 'Mach-O/' + self.magicNumber + '\n' + \
                'Arch: ' + self.arch + '\n' + \
                'Filetype: ' + self.filetype + '\n' + \
                'Symbols: ' + self.symbolsCount + '\n' + \
                'Tool Version: ' + self.toolVersion + '\n' + \
                'File Version: ' + self.fileVersion + '\n' + \
                'UUID: ' + self.uuid + '\n' + \
                'Built Time: ' + self.buildTime + '\n' + \
                'Symbol table: ' + '\n' + self.symbolTable

    # 根据获取的cpu值转换为cpu架构描述
    def getMachine(self, cputype):

        CPU_ARCH_ABI64 = 0x01000000		# 64 bit ABI
        CPU_TYPE_ARM = 12
        CPU_TYPE_POWERPC = 18
        CPU_TYPE_X86 = 7

        if cputype == CPU_TYPE_X86:
            return "X86"
        elif cputype == CPU_TYPE_X86 | CPU_ARCH_ABI64:
            return "X86_64"
        elif cputype == CPU_TYPE_POWERPC:
            return "PPC"
        elif cputype == CPU_TYPE_POWERPC | CPU_ARCH_ABI64:
            return "PPC64"
        elif cputype == CPU_TYPE_ARM:
            return "ARM"
        elif cputype == CPU_TYPE_ARM | CPU_ARCH_ABI64:
            return "ARM64"
        else:
            return '???'

    # 文件类型决定mach-o布局格式
    def getFiletype(self, fileType):
        # 编译过程中产生的  obj文件 (gcc -c xxx.c 生成xxx.o文件)
        MH_OBJECT	= 0x1
        # 可执行二进制文件 (/usr/bin/ls)
        MH_EXECUTE	= 0x2
        MH_FVMLIB	= 0x3		# fixed VM shared library file */
        MH_CORE		= 0x4		# CoreDump (崩溃时的Dump文件)
        MH_PRELOAD	= 0x5		# preloaded executable file */
        MH_DYLIB	= 0x6		# 动态库(/usr/lib/里面的那些共享库文件)
        MH_DYLINKER	= 0x7		# 连接器linker（/usr/lib/dyld文件）
        MH_BUNDLE	= 0x8		# dynamically bound bundle file */
        MH_DYLIB_STUB = 0x9		# shared library stub for static */
        MH_DSYM	= 0xa		# companion file with only debug */
        MH_KEXT_BUNDLE = 0xb		# 内核扩展文件 （自己开发的简单内核模块）

        if MH_OBJECT == fileType:
            return 'Object'
        elif MH_EXECUTE == fileType:
            return 'Executable'
        elif MH_FVMLIB == fileType:
            return 'Fixed VM Shared Library'
        elif MH_CORE == fileType:
            return 'Core'
        elif MH_PRELOAD == fileType:
            return 'Preloaded Executable'
        elif MH_DYLIB == fileType:
            return 'Shared Library'
        elif MH_DYLINKER == fileType:
            return 'Dynamic Link Editor'
        elif MH_BUNDLE == fileType:
            return 'Bundle'
        elif MH_DYLIB_STUB == fileType:
            return 'Shared Library Stub'
        elif MH_DSYM == fileType:
            return 'Debug Symbols'
        elif MH_KEXT_BUNDLE == fileType:
            return 'Kernel Extension'
        else:
            return '???'


if __name__ == '__main__':
    mach = Mach()
    print(mach.description())