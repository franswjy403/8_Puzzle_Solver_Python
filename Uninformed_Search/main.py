from time import time
from BFS import breadth_first_search
from DLS import depth_limited_search
from puzzleBoard import Puzzle

state=[ [2,8,3,
         1,6,4,
         7,0,5],
         
         [8,3,2,
         6,1,4,
         5,0,7]]

for i in range(0,2):

    Puzzle.num_of_instances = 0
    t0 = time()
    BFS = breadth_first_search(state[i])
    t1 = time() - t0
    print('BFS:',BFS)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()

    depth = [5, 7, 10, 15, 20]
    for d in depth:
        Puzzle.num_of_instances = 0
        t0 = time()
        DLS = depth_limited_search(state[i], d)
        t1 = time() - t0
        print('DLS:',DLS)
        print('depth limit:', d)
        print('space:', Puzzle.num_of_instances)
        print('time:', t1)
        print()

    print('------------------------------------------')

'''
Perbandingan hasil BFS dengan DLS :

BFS: ['U', 'U', 'L', 'D', 'R']
space: 54
time: 0.0010020732879638672

DLS: ['U', 'U', 'L', 'D', 'R']
depth limit: 5
space: 93
time: 0.0010013580322265625

DLS: ['U', 'U', 'L', 'D', 'R']
depth limit: 7
space: 253
time: 0.0030014514923095703

DLS: ['U', 'U', 'L', 'D', 'R']
depth limit: 10
space: 816
time: 0.024999380111694336

DLS: ['R', 'U', 'L', 'L', 'U', 'R', 'D', 'R', 'D', 'L', 'U', 'L', 'U', 'R', 'D']
depth limit: 15
space: 812
time: 0.025993824005126953

DLS: ['R', 'U', 'L', 'D', 'R', 'U', 'L', 'L', 'U', 'R', 'D', 'L', 'U', 'R', 'D', 'D', 'R', 'U', 'L']
depth limit: 20
space: 3673
time: 0.2620222568511963

------------------------------------------
BFS: ['R', 'U', 'U', 'L', 'D', 'D', 'L', 'U', 'R', 'R', 'D', 'L', 'L', 'U', 'U', 'R', 'D']
space: 39933
time: 14.346549034118652

DLS: None
depth limit: 5
space: 93
time: 0.0010042190551757812

DLS: None
depth limit: 7
space: 271
time: 0.0050220489501953125

DLS: None
depth limit: 10
space: 911
time: 0.02801656723022461

DLS: None
depth limit: 15
space: 3939
time: 0.25199294090270996

DLS: ['R', 'U', 'L', 'D', 'L', 'U', 'R', 'R', 'U', 'L', 'D', 'R', 'D', 'L', 'L', 'U', 'U', 'R', 'D']
depth limit: 20
space: 5304
time: 0.43799686431884766
'''