from df_matrix import df_matrix, OccupiedCellError, BrokenConstraintError
import numpy as np
import random
import time
import copy


def search(board,depth=0):
    
    #time.sleep(0.3)
    
    if np.sum(board.dfs)>0:

        mostconst = board.get_mostconst()
        print('====')
        print(board)
        print('depth: {}'.format(depth))
        print('----')
        for cell in range(mostconst.shape[0]):
            i = mostconst[cell,0]
            j = mostconst[cell,1]
        
            possible_set = board.domain-board.get_constraints(i,j)

            print(len(possible_set))

            for pv in possible_set:
                child = copy.deepcopy(board)
                try:
                    child.add_symbol(i,j,pv)
                    search(child,depth+1)
                except OccupiedCellError:
                    print('sciao')
                except BrokenConstraintError:
                    print('belo')
    
    elif np.sum(board.matrix==0) == 0:
        print(board)


if __name__ == '__main__':

    c = 9**81

    print(c)

    board = df_matrix()

    board.import_data('data.csv')

    print(board)

    search(board)

