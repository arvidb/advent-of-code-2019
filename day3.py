'''input
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
'''
import operator
import sys

w1 = input().split(',')
w2 = input().split(',')

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

coords = {}
orig = (0,0)
steps = 0
for path in w1:
    dir = path[0]   
    for _ in range(int(path[1:])):
        orig = tuple(map(operator.add, orig, dirs[dir]))
        steps += 1
        coords[orig] = steps        

orig = (0,0)
steps = 0
best = (sys.maxsize, None)
for path in w2:
    dir = path[0]   
    for _ in range(int(path[1:])):
        orig = tuple(map(operator.add, orig, dirs[dir]))
        steps += 1
        if orig in coords:      
            steps1 = coords[orig]   
            sum_steps = steps1 + steps
            #dist = abs(orig[0]) + abs(orig[1])
            if sum_steps < best[0]:
                best = (sum_steps, orig)            

print(best[0])


