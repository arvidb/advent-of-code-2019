grid = []
try:
    while True:
        grid.append([c for c in input()])
except:
    pass

def find_repeating_state():
    states = []
    while True:
        grid2 = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                for xa, ya in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x2, y2 = xa + x, ya + y
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[x]):
                        if grid[y2][x2] == '#':
                            grid2[y][x] += 1

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                has_bug = grid[y][x] == '#'
                if has_bug and grid2[y][x] != 1:
                    grid[y][x] = '.'
                elif not has_bug and grid2[y][x] in (1, 2):
                    grid[y][x] = '#'
        
        state = ''.join([c for row in grid for c in row])
        if state in states:
            return grid
        else:
            states.append(state)

grid = find_repeating_state()

score = [1 << (len(grid[0])*y + (1+x) - 1) if grid[y][x] == '#' else 0 for y in range(len(grid)) for
    x in range(len(grid[y]))]
print('Part 1', sum(score))
