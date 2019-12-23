import operator
import sys

grid = {}
player_pos = (0,0)
try:
    y = 0
    while True:
        for x, c in enumerate(input()):
            grid[(x, y)] = c
            if c == '@':
                player_pos = (x, y)
                grid[player_pos] = '.'
        y += 1
except:
    pass

key_count = sum([x.islower() for x in grid.values()])

def bfs(start_pos):
    memo = {}
    q = []
    q.append((start_pos, set(), 0))

    best_path = sys.maxsize
    while q:
        pos, keys, steps = q.pop(0)

        if len(keys) == key_count:
            best_path = min(steps, best_path)
            break
        
        tile = grid.get(pos)
        if tile.islower():
            keys.add(tile)
        elif tile.isupper() and tile.lower() not in keys:
            continue
        
        key = (pos[0], pos[1], ''.join(keys))
        memo_dist = memo.get(key, sys.maxsize)
        if steps >= memo_dist:
            continue
        else:
            memo[key] = steps

        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_pos = tuple(map(operator.add, pos, direction))
            if new_pos in grid and grid[new_pos] != '#':
                q.append((new_pos, keys.copy(), steps+1))

    return best_path-1

print('Part 1', bfs(player_pos))
