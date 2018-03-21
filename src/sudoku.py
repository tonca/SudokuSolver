import numpy as np


class sudoku:

    domain = set(range(1,10))
    
    def __init__(self):
        self.sudoku = np.zeros((9,9), dtype=int)

    def add_symbol(self,i,j,sym):
        if not sym in self.domain:
            raise InvalidSymbolError()
        self.sudoku[i,j] = sym

    def get_symbol(self,i,j):
        return self.sudoku[i,j]    

    def __str__(self):

        sep = '+-------+-------+-------+\n'
        out = ''
        for i in range(0,9):

            if i%3 == 0:
                out = out + sep
            
            for j in range(0,9):
                if j%3 == 0:
                    out = out + '| '

                if int(self.get_symbol(i,j)) == 0:
                    sym = ' '
                else:
                    sym = str(self.get_symbol(i,j))
                out = out + sym + ' ' 

            out = out + '|\n'

        out = out + sep

        return out

class InvalidSymbolError(Exception):
    pass

if __name__ == '__main__':

    test = sudoku()

    test.add_symbol(0,7,9)
    test.add_symbol(6,3,7)
    test.add_symbol(3,3,2)
    test.add_symbol(1,8,1)

    print(test)