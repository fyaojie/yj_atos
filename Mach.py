# coding=utf-8
from os import nice, path
from SegmentCommand64 import SegmentCommand64
from Symbol import Symbol
from Symtab import Symtab

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

    # 符号表配置
    symtab = Symtab()
    # 符号相关信息
    symbols = []

    segments = []

    def description(self):
        return  'File: ' + self.path + '\n' + \
                'Format: ' + 'Mach-O/' + self.magicNumber + '\n' + \
                'Symtab: ' + self.symtab.description() + '\n' + \
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

        #         /*
#  * After MacOS X 10.1 when a new load command is added that is required to be
#  * understood by the dynamic linker for the image to execute properly the
#  * LC_REQ_DYLD bit will be or'ed into the load command constant.  If the dynamic
#  * linker sees such a load command it it does not understand will issue a
#  * "unknown load command required for execution" error and refuse to use the
#  * image.  Other load commands without this bit that are not understood will
#  * simply be ignored.
#  */
# #define LC_REQ_DYLD 0x80000000

# /* Constants for the cmd field of all load commands, the type */
# #define	LC_SEGMENT	0x1	/* segment of this file to be mapped */
# #define	LC_SYMTAB	0x2	/* link-edit stab symbol table info */
# #define	LC_SYMSEG	0x3	/* link-edit gdb symbol table info (obsolete) */
# #define	LC_THREAD	0x4	/* thread */
# #define	LC_UNIXTHREAD	0x5	/* unix thread (includes a stack) */
# #define	LC_LOADFVMLIB	0x6	/* load a specified fixed VM shared library */
# #define	LC_IDFVMLIB	0x7	/* fixed VM shared library identification */
# #define	LC_IDENT	0x8	/* object identification info (obsolete) */
# #define LC_FVMFILE	0x9	/* fixed VM file inclusion (internal use) */
# #define LC_PREPAGE      0xa     /* prepage command (internal use) */
# #define	LC_DYSYMTAB	0xb	/* dynamic link-edit symbol table info */
# #define	LC_LOAD_DYLIB	0xc	/* load a dynamically linked shared library */
# #define	LC_ID_DYLIB	0xd	/* dynamically linked shared lib ident */
# #define LC_LOAD_DYLINKER 0xe	/* load a dynamic linker */
# #define LC_ID_DYLINKER	0xf	/* dynamic linker identification */
# #define	LC_PREBOUND_DYLIB 0x10	/* modules prebound for a dynamically */
# 				/*  linked shared library */
# #define	LC_ROUTINES	0x11	/* image routines */
# #define	LC_SUB_FRAMEWORK 0x12	/* sub framework */
# #define	LC_SUB_UMBRELLA 0x13	/* sub umbrella */
# #define	LC_SUB_CLIENT	0x14	/* sub client */
# #define	LC_SUB_LIBRARY  0x15	/* sub library */
# #define	LC_TWOLEVEL_HINTS 0x16	/* two-level namespace lookup hints */
# #define	LC_PREBIND_CKSUM  0x17	/* prebind checksum */

# /*
#  * load a dynamically linked shared library that is allowed to be missing
#  * (all symbols are weak imported).
#  */
# #define	LC_LOAD_WEAK_DYLIB (0x18 | LC_REQ_DYLD)

# #define	LC_SEGMENT_64	0x19	/* 64-bit segment of this file to be
# 				   mapped */
# #define	LC_ROUTINES_64	0x1a	/* 64-bit image routines */
# #define LC_UUID		0x1b	/* the uuid */
# #define LC_RPATH       (0x1c | LC_REQ_DYLD)    /* runpath additions */
# #define LC_CODE_SIGNATURE 0x1d	/* local of code signature */
# #define LC_SEGMENT_SPLIT_INFO 0x1e /* local of info to split segments */
# #define LC_REEXPORT_DYLIB (0x1f | LC_REQ_DYLD) /* load and re-export dylib */
# #define	LC_LAZY_LOAD_DYLIB 0x20	/* delay load of dylib until first use */
# #define	LC_ENCRYPTION_INFO 0x21	/* encrypted segment information */
# #define	LC_DYLD_INFO 	0x22	/* compressed dyld information */
# #define	LC_DYLD_INFO_ONLY (0x22|LC_REQ_DYLD)	/* compressed dyld information only */
# #define	LC_LOAD_UPWARD_DYLIB (0x23 | LC_REQ_DYLD) /* load upward dylib */
# #define LC_VERSION_MIN_MACOSX 0x24   /* build for MacOSX min OS version */
# #define LC_VERSION_MIN_IPHONEOS 0x25 /* build for iPhoneOS min OS version */
# #define LC_FUNCTION_STARTS 0x26 /* compressed table of function start addresses */
# #define LC_DYLD_ENVIRONMENT 0x27 /* string for dyld to treat
# 				    like environment variable */
# #define LC_MAIN (0x28|LC_REQ_DYLD) /* replacement for LC_UNIXTHREAD */
# #define LC_DATA_IN_CODE 0x29 /* table of non-instructions in __text */
# #define LC_SOURCE_VERSION 0x2A /* source version used to build binary */
# #define LC_DYLIB_CODE_SIGN_DRS 0x2B /* Code signing DRs copied from linked dylibs */
# #define	LC_ENCRYPTION_INFO_64 0x2C /* 64-bit encrypted segment information */
# #define LC_LINKER_OPTION 0x2D /* linker options in MH_OBJECT files */
# #define LC_LINKER_OPTIMIZATION_HINT 0x2E /* optimization hints in MH_OBJECT files */
    def loadCommand(self, cmd):
        LC_REQ_DYLD = 0x80000000
        loadCommandDict = {
            0x1: 'LC_SEGMENT',
            0x2: 'LC_SYMTAB',
            0x3: 'LC_SYMSEG',
            0x4: 'LC_THREAD',
            0x5: 'LC_UNIXTHREAD',
            0x6: 'LC_LOADFVMLIB',
            0x7: 'LC_IDFVMLIB',
            0x8: 'LC_IDENT',
            0x9: 'LC_FVMFILE',
            0xa: 'LC_PREPAGE',
            0xb: 'LC_DYSYMTAB',
            0xc: 'LC_LOAD_DYLIB',
            0xd: 'LC_ID_DYLIB',
            0xe: 'LC_LOAD_DYLINKER',
            0xf: 'LC_ID_DYLINKER',
            0x10: 'LC_PREBOUND_DYLIB',

            0x11: 'LC_ROUTINES',
            0x12: 'LC_SUB_FRAMEWORK',
            0x13: 'LC_SUB_UMBRELLA',
            0x14: 'LC_SUB_CLIENT',
            0x15: 'LC_SUB_LIBRARY',
            0x16: 'LC_TWOLEVEL_HINTS',
            0x17: 'LC_PREBIND_CKSUM',

            (0x18 | LC_REQ_DYLD): 'LC_LOAD_WEAK_DYLIB',
            0x19: 'LC_SEGMENT_64',
            0x1a: 'LC_ROUTINES_64',
            0x1b: 'LC_UUID',
            (0x1c | LC_REQ_DYLD): 'LC_RPATH',
            0x1d: 'LC_CODE_SIGNATURE',
            0x1e: 'LC_SEGMENT_SPLIT_INFO',
            (0x1f | LC_REQ_DYLD): 'LC_REEXPORT_DYLIB',
            0x20: 'LC_LAZY_LOAD_DYLIB',
            0x21: 'LC_ENCRYPTION_INFO',
            0x22: 'LC_DYLD_INFO',
            (0x22|LC_REQ_DYLD): 'LC_DYLD_INFO_ONLY',
            (0x23 | LC_REQ_DYLD): 'LC_LOAD_UPWARD_DYLIB',
            0x24: 'LC_VERSION_MIN_MACOSX',
            0x25: 'LC_VERSION_MIN_IPHONEOS',
            0x26: 'LC_FUNCTION_STARTS',
            0x27: 'LC_DYLD_ENVIRONMENT',
            (0x28|LC_REQ_DYLD): 'LC_MAIN',
            0x29: 'LC_DATA_IN_CODE',
            0x2A: 'LC_SOURCE_VERSION',
            0x2B: 'LC_DYLIB_CODE_SIGN_DRS',
            0x2C: 'LC_ENCRYPTION_INFO_64',
            0x2D: 'LC_LINKER_OPTION',
            0x2E: 'LC_LINKER_OPTIMIZATION_HINT'
        }
        value = loadCommandDict.get(cmd)
        if not value:
            return '???'
        return value



if __name__ == '__main__':
    mach = Mach()
    print(mach.description())
    print(mach.loadCommand(0x111))
    print(mach.segment)