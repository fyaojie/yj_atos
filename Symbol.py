
class Symbol:
    # 索引到字符串表中
    n_strx = 0
    # 类型标志
    n_type = 0
    # section编号或NO_SECT
    n_sect = 0
    n_desc = 0
    # 该符号的值(或戳偏移量)
    n_value = 0

    address = ''

    # 下一个索引的位置,用于计算当前的符号长度
    # next_n_strx = 0
    # 符号长度
    lenth = 1

    def setNextStrx(self, next_n_strx):
        # self.next_n_strx = next_n_strx
        self.lenth = next_n_strx - self.n_strx
        if self.lenth <= 0:
            self.lenth = 1
        if self.lenth > 100:
            print(self.lenth)
            print(self.n_strx)
            print(next_n_strx)

    def __init__(self, strx, type, sect, desc, value) -> None:
        self.n_strx = strx
        self.n_type = type
        self.n_sect = sect
        self.n_desc = desc
        self.n_value = value
        self.address = hex(self.n_value).upper()


    def description(self):
        return  '   索引: ' + str(self.n_strx) + '\n' + \
                '   类型标志: ' + str(self.n_type) + '\n' + \
                '   编号: ' + str(self.n_sect) + '\n' + \
                '   描述: ' + str(self.n_desc) + '\n' + \
                '   长度: ' + str(self.lenth) + '\n' + \
                '   偏移量(10进制): ' + str(self.n_value) + '\n' + \
                '   偏移量(16进制): ' + str(self.address)

if __name__ == '__main__':
    sym = Symbol(10, 10, 10, 10, 10)
    sym.setNextStrx(30)
    print(sym.description())
