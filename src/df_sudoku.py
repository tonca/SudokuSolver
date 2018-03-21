from sudoku import sudoku
import numpy as np


class df_sudoku(sudoku):


    def __init__(self):
        sudoku.__init__(self)
        self.dfs = np.ones((9,9), dtype=int)*9


    def add_symbol(self,i,j,sym):
        self.check_valid(i,j,sym)
        super(df_sudoku, self).add_symbol(i,j,sym)
        self.update_dfs()


    def get_df(self,i,j):
        return self.dfs[i,j]


    def compute_df(self,i,j):
        if self.get_symbol(i,j) != 0:
            return 0

        const_set = self.get_constraints(i,j)

        return 9-len(const_set)


    def update_dfs(self):
        for i in range(0,9):
            for j in range(0,9):
                self.dfs[i,j] = self.compute_df(i,j)


    def check_valid(self,i,j,sym):
        if self.get_symbol(i,j) != 0:
            raise OccupiedCellError('Cell ({},{}) already assigned!'.format(i,j))

        const_set = self.get_constraints(i,j)
        if sym in const_set:
            raise BrokenConstraintError('{} in position ({},{}) breaks the constraints!'.format(sym,i,j))


    def get_constraints(self,i,j):

        # Cell already taken
        if self.get_symbol(i,j) != 0:
            return self.domain

        # Constraints
        row_const = self.sudoku[i,:]
        row_set = set(row_const)

        col_const = self.sudoku[:,j]
        col_set = set(col_const)

        block_i = np.int(np.floor(i/3))*3
        block_j = np.int(np.floor(j/3))*3
        block_const = self.sudoku[block_i:block_i+3,block_j:block_j+3].flatten()
        block_set = set(block_const)

        # Merge
        const_set = row_set | col_set | block_set
        const_set.discard(0)

        return const_set


    def get_freeCells(self):
        return np.transpose(np.where(self.sudoku==0))


    def get_mostconst(self):
        min_df = np.min(self.dfs[np.nonzero(self.dfs)])
        return np.transpose(np.where(self.dfs==min_df))


    def to_hash(self):
        hash = 0
        for i in range(9):
            for j in range(9):
                hash = hash + 9**(i*9+j)*int(self.get_symbol(i,j))
        return hash


    def import_data(self,file):
        self.sudoku = np.genfromtxt(file, delimiter=',', dtype=int)
        self.update_dfs()


    def __str__(self):

        sep = '+-------+-------+-------+  +-------+-------+-------+\n'
        out = ''
        for i in range(0,9):

            if i%3 == 0:
                out = out + sep
            
            # Symbols            
            for j in range(0,9):
                if j%3 == 0:
                    out = out + '| '

                if int(self.get_symbol(i,j)) == 0:
                    sym = '.'
                else:
                    sym = str(self.get_symbol(i,j))
                out = out + sym + ' ' 

            out = out + '|  '

            # DFs
            for j in range(0,9):  
                
                if j%3 == 0:
                    out = out + '| '

                if int(self.get_df(i,j)) == 0:
                    sym = '.'
                else:
                    sym = str(self.get_df(i,j))
                out = out + sym + ' '

            out = out + '|\n'

        out = out + sep

        return out


class BrokenConstraintError(Exception):
    pass

class OccupiedCellError(Exception):
    pass



if __name__ == '__main__':

    test = df_sudoku()

    test.add_symbol(0,7,9)
    test.add_symbol(6,3,7)
    test.add_symbol(3,3,2)
    test.add_symbol(4,1,2)


    test.update_dfs()
    print(test)