# /*
#  * The 64-bit segment load command indicates that a part of this file is to be
#  * mapped into a 64-bit task's address space.  If the 64-bit segment has
#  * sections then section_64 structures directly follow the 64-bit segment
#  * command and their size is reflected in cmdsize.
#  */
# typedef int             vm_prot_t;
# struct segment_command_64 { /* for 64-bit architectures */
# 	uint32_t	cmd;		/* LC_SEGMENT_64 */
# 	uint32_t	cmdsize;	/* includes sizeof section_64 structs */
# 	char		segname[16];	/* segment name */
# 	uint64_t	vmaddr;		/* memory address of this segment */
# 	uint64_t	vmsize;		/* memory size of this segment */
# 	uint64_t	fileoff;	/* file offset of this segment */
# 	uint64_t	filesize;	/* amount to map from the file */
# 	vm_prot_t	maxprot;	/* maximum VM protection */
# 	vm_prot_t	initprot;	/* initial VM protection */
# 	uint32_t	nsects;		/* number of sections in segment */
# 	uint32_t	flags;		/* flags */
# };

class SegmentCommand64:
    cmd = 0
    cmdsize = 0
    segname = ''
    vmaddr = 0
    vmsize = 0
    fileoff = 0
    filesize = 0
    maxprot = 0
    initprot = 0
    nsects = 0
    flags = 0

if __name__ == '__main__':
    sym = SegmentCommand64()
    print(sym)