# coding=utf-8
import struct
import sys
import os

from Mach import Mach

# https://www.jianshu.com/p/c07e5ee89b3e
# https://blog.csdn.net/zhangyutangde/article/details/78339143?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.no_search_link&spm=1001.2101.3001.4242.1
# http://blog.tingyun.com/web/article/detail/1341
# https://www.sohu.com/a/437063227_571478

# dwarfdump -F --debug-line /Users/symbio/Desktop/CMSTest.app.dSYM > line-e.txt
# nm /Users/symbio/Desktop/CMSTest.app.dSYM/Contents/Resources/DWARF/CMSTest

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
