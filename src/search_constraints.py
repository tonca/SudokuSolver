from df_sudoku import df_sudoku, OccupiedCellError, BrokenConstraintError
import numpy as np
import random
import time
import copy


# Depth first search
def search(board,depth=0):
    
    solutions = []

    if np.sum(board.sudoku==0)==0:
        return [board]
    elif np.sum(board.dfs)==0:
        return []

    mostconst = board.get_mostconst()
    
    randid = np.random.randint(mostconst.shape[0])

    i = mostconst[randid,0]
    j = mostconst[randid,1]

    possible_set = board.domain-board.get_constraints(i,j)

    for pv in possible_set:
        child = copy.deepcopy(board)
        try:
            child.add_symbol(i,j,pv)
            subsolutions = search(child,depth+1)
            solutions = solutions + subsolutions

        except OccupiedCellError:
            print('sciau')
        except BrokenConstraintError:
            print('belo')

    return solutions



if __name__ == '__main__':

    board = df_sudoku()

    board.import_data('data/extreme.csv')

    print(board)
    start_time = time.time()

    solutions = search(board)

    elapsed_time = time.time() - start_time

    print('SOLUTIONS: {}'.format(len(solutions)))
    hashes = []
    for sol in solutions:
        print(sol)
        hashes.append(sol.to_hash())
    print('SOLUTIONS: {}'.format(len(solutions)))
    print('UNIQUE SOLUTIONS: {}'.format(len(set(hashes))))

    print('elapsed_time:'+str(elapsed_time))