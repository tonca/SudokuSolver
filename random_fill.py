from df_matrix import df_matrix, OccupiedCellError, BrokenConstraintError
import numpy as np
import random
import time


if __name__ == '__main__':

    board = df_matrix()
    freecells = board.get_freeCells()

    while np.sum(board.dfs)>0:

        freecells = board.get_freeCells()
        randid = np.random.randint(freecells.shape[0])

        i = freecells[randid,0]
        j = freecells[randid,1]
        
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
            time.sleep(.1)
        else:
            continue

