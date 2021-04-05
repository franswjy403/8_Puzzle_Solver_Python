from time import time
from AStar import Astar_search
from RBFS import recursive_best_first_search
from puzzleBoard import Puzzle

state=[ [4, 7, 2,
        6, 5, 0,
        1, 3, 8],

        [7, 2, 4,
        5, 0, 6,
        8, 3, 1]]

for i in range(0,2):

    Puzzle.num_of_instances = 0
    t0 = time()
    astar = Astar_search(state[i])
    t1 = time() - t0
    print('A*:',astar)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()

    Puzzle.num_of_instances = 0
    t0 = time()
    RBFS = recursive_best_first_search(state[i])
    t1 = time() - t0
    print('RBFS:',RBFS)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()

    print('------------------------------------------')

'''
Perbandingan hasil A* dan RBFS :

A*: ['L', 'L', 'D', 'R', 'U', 'U', 'L', 'D', 'D', 'R', 'U', 'U', 'L']
space: 119
time: 0.0030219554901123047

RBFS: ['L', 'L', 'D', 'R', 'U', 'U', 'L', 'D', 'D', 'R', 'U', 'U', 'L']
space: 349
time: 0.015987396240234375

------------------------------------------
A*: ['L', 'U', 'R', 'D', 'D', 'L', 'U', 'R', 'R', 'U', 'L', 'L', 'D', 'R', 'R', 'D', 'L', 'L', 'U', 'R', 'R', 'U', 'L', 'D', 'L', 'U']
space: 19622
time: 7.435999393463135

RBFS: ['L', 'U', 'R', 'D', 'D', 'L', 'U', 'R', 'R', 'U', 'L', 'L', 'D', 'R', 'R', 'D', 'L', 'L', 'U', 'R', 'R', 'U', 'L', 'D', 'L', 'U']
space: 1503095
time: 29.423022031784058
'''