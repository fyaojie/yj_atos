# /*
#  * A segment is made up of zero or more sections.  Non-MH_OBJECT files have
#  * all of their segments with the proper sections in each, and padded to the
#  * specified segment alignment when produced by the link editor.  The first
#  * segment of a MH_EXECUTE and MH_FVMLIB format file contains the mach_header
#  * and load commands of the object file before its first section.  The zero
#  * fill sections are always last in their segment (in all formats).  This
#  * allows the zeroed segment padding to be mapped into memory where zero fill
#  * sections might be. The gigabyte zero fill sections, those with the section
#  * type S_GB_ZEROFILL, can only be in a segment with sections of this type.
#  * These segments are then placed after all other segments.
#  *
#  * The MH_OBJECT format has all of its sections in one segment for
#  * compactness.  There is no padding to a specified segment boundary and the
#  * mach_header and load commands are not part of the segment.
#  *
#  * Sections with the same section name, sectname, going into the same segment,
#  * segname, are combined by the link editor.  The resulting section is aligned
#  * to the maximum alignment of the combined sections and is the new section's
#  * alignment.  The combined sections are aligned to their original alignment in
#  * the combined section.  Any padded bytes to get the specified alignment are
#  * zeroed.
#  *
#  * The format of the relocation entries referenced by the reloff and nreloc
#  * fields of the section structure for mach object files is described in the
#  * header file <reloc.h>.
#  */
# struct section { /* for 32-bit architectures */
# 	char		sectname[16];	/* name of this section */
# 	char		segname[16];	/* segment this section goes in */
# 	uint32_t	addr;		/* memory address of this section */
# 	uint32_t	size;		/* size in bytes of this section */
# 	uint32_t	offset;		/* file offset of this section */
# 	uint32_t	align;		/* section alignment (power of 2) */
# 	uint32_t	reloff;		/* file offset of relocation entries */
# 	uint32_t	nreloc;		/* number of relocation entries */
# 	uint32_t	flags;		/* flags (section type and attributes)*/
# 	uint32_t	reserved1;	/* reserved (for offset or index) */
# 	uint32_t	reserved2;	/* reserved (for count or sizeof) */
# };

# struct section_64 { /* for 64-bit architectures */
# 	char		sectname[16];	/* name of this section */
# 	char		segname[16];	/* segment this section goes in */
# 	uint64_t	addr;		/* memory address of this section */
# 	uint64_t	size;		/* size in bytes of this section */
# 	uint32_t	offset;		/* file offset of this section */
# 	uint32_t	align;		/* section alignment (power of 2) */
# 	uint32_t	reloff;		/* file offset of relocation entries */
# 	uint32_t	nreloc;		/* number of relocation entries */
# 	uint32_t	flags;		/* flags (section type and attributes)*/
# 	uint32_t	reserved1;	/* reserved (for offset or index) */
# 	uint32_t	reserved2;	/* reserved (for count or sizeof) */
# 	uint32_t	reserved3;	/* reserved */
# };

# <16s16sQQIIIIIIII
class Section64:
   sectname = ''
   segname = ''
   addr = 0
   size = 0
   offset = 0
   align = 0
   reloff = 0
   nreloc = 0
   flags = 0
   reserved1 = 0
   reserved2 = 0
   reserved3 = 0

   def __init__(self, value) -> None:
      self.sectname = value[0]
      self.segname = value[1]
      self.addr = value[2]
      self.size = value[3]
      self.offset = value[4]
      self.align = value[5]
      self.reloff = value[6]
      self.nreloc = value[7]
      self.flags = value[8]
      self.reserved1 = value[9]
      self.reserved2 = value[10]
      self.reserved3 = value[11]



if __name__ == '__main__':
   sym = Section64()
   print(sym)