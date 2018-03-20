from df_matrix import df_matrix, OccupiedCellError, BrokenConstraintError
import numpy as np
import random
import time


if __name__ == '__main__':

    board = df_matrix()

    board.import_data('data.csv')

    print(board)

    while np.sum(board.dfs)>0:

        # The Node-consistency approach
        mostconst = board.get_mostconst()

        randid = np.random.randint(mostconst.shape[0])

        i = mostconst[randid,0]
        j = mostconst[randid,1]
        
        possible_set = board.domain-board.get_constraints(i,j)
        
        if len(possible_set)>0:
            sym = random.sample(possible_set, 1)[0]
            try:
                board.add_symbol(i,j,sym)
            except OccupiedCellError:
                print('sciao')
            except BrokenConstraintError:
                print('belo')
            print(board)
        else:
            continue

