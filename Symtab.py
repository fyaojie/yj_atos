from ctypes import sizeof
class Symtab:
    cmd = 0 # LC_SYMTAB
    cmdsize = 0 # sizeof(Symtab)
    symoff = 0 # symbol table offset
    nsyms = 0 # number of symbol table entries
    stroff = 0 # string table offset
    strsize = 0 # string table size in bytes

    def description(self):
        return  '   cmd: LC_SYMTAB' + '\n' + \
                '   cmdsize: ' + str(self.cmdsize) + '\n' + \
                '   symbol table offset: ' + str(self.symoff) + '\n' + \
                '   number of symbol table entries: ' + str(self.nsyms) + '\n' + \
                '   string table offset: ' + str(self.stroff) + '\n' + \
                '   string table size in bytes: ' + str(self.strsize)

if __name__ == '__main__':
    sym = Symtab()
    print(sym.description())