import sys

portals = {}
portals2 = {}
board = {}

y = 0
while True:
    try:
        for x, c in enumerate(input()):
            board[(x, y)] = c
            if c.isalpha():
                for peak in [(0, -1), (-1, 0)]:
                    p1 = x + peak[0], y + peak[1]
                    peak_char = board.get(p1, '')
                    if peak_char != '' and peak_char.isalpha():
                        name = peak_char + c
                        p2 = (x, y)
                        portals[p1] = name
                        portals[p2] = name
                        if name in portals2:
                            portals2[name].append([p1, p2])
                        else:
                            portals2[name] = [[p1, p2]]
        y += 1
    except:
        break


def find_portal_passage(cur_pos, portal):
    for portal in portals2[portal]:
        if cur_pos in portal:
            continue
        for pos in portal:
            for peak in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                x, y = pos
                peak_pos = (x + peak[0], y + peak[1])
                peak_char = board.get(peak_pos, '')
                if peak_char == '.':
                    yield peak_pos

def dfs(start_pos):

    stack = []
    stack.append((start_pos, set(), 0, set(['AA'])))

    best_path = sys.maxsize
    while len(stack):
        pos, seen, steps, taken_portals = stack[-1]
        stack.pop()
        
        if pos not in board:
            continue

        tile = board[pos]
        if tile == '#':
            continue

        if tile.isalpha():
            # portal
            portal = portals[pos]
            if portal == 'ZZ':
                print('found end', steps-1, taken_portals)
                best_path = min(best_path, steps-1)
                continue
            else:
                if portal in taken_portals:
                    continue
                taken_portals.add(portal)
                for new_pos in find_portal_passage(pos, portal):
                    pos = new_pos

        # path
        for peak in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            new_pos = pos[0] + peak[0], pos[1] + peak[1]
            if new_pos in seen:
                continue

            new_seen = seen.copy()
            new_seen.add(new_pos)
            stack.append((new_pos, new_seen, steps + 1, taken_portals.copy()))
        
    return best_path

start_pos = next(find_portal_passage((0,0), 'AA'))
print('Part 1', dfs(start_pos))
