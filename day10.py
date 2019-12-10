'''input
##.##..#.####...#.#.####
##.###..##.#######..##..
..######.###.#.##.######
.#######.####.##.#.###.#
..#...##.#.....#####..##
#..###.#...#..###.#..#..
###..#.##.####.#..##..##
.##.##....###.#..#....#.
########..#####..#######
##..#..##.#..##.#.#.#..#
##.#.##.######.#####....
###.##...#.##...#.######
###...##.####..##..#####
##.#...#.#.....######.##
.#...####..####.##...##.
#.#########..###..#.####
#.##..###.#.######.#####
##..##.##...####.#...##.
###...###.##.####.#.##..
####.#.....###..#.####.#
##.####..##.#.##..##.#.#
#####..#...####..##..#.#
.##.##.##...###.##...###
..###.########.#.###..#.
'''
import math
import collections

grid = []
try:
	while True:
		line = input()
		if line:
			grid.append(list(line))
		else:
			break
except:
	pass

asteroids = [(x, y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == '#']

def calc_angle(from_pos, to_pos):
	x1, y1 = from_pos
	x2, y2 = to_pos
	dx = x2-x1
	dy = y2-y1

	angle = math.atan2(dx, dy)
	
	if angle < 0.0:
		angle += 2 * math.pi

	if angle != 0.0:
		angle = 2 * math.pi - angle

	dist = math.sqrt(dx**2 + dy**2)
	return (angle, dist)

best = 0
best_pos = None
for source in asteroids:
	rays = {}
	for target in asteroids:
		if target == source:
			continue
		angle, dist = calc_angle(source, target)
		rays[angle] = dist

	if len(rays) > best:
		best_pos = source
		best = len(rays)

print('Answer 1:', best, best_pos)
base = best_pos

rays = {}
for target in asteroids:
	if target == base:
		continue
	angle, dist = calc_angle(base, target)
	if not angle in rays:
		rays[angle] = []
	rays[angle].append((dist, target))
	rays[angle].sort(key=lambda x: x[0], reverse=False)

ordered_rays = collections.OrderedDict(sorted(rays.items()))

count = 0
while count < 200:
	min_angle = None
	l = []
	r = []
	for angle, x in ordered_rays.items():
		if angle >= math.pi:
			r.append(x)
		else:
			l.append(x)

	for x in r + l:
		if len(x) == 0:
			continue
		else:
			last_value = x.pop(0)
			count += 1

		if count == 200:
			_, pos = last_value
			print('Answer 2:', pos[0] * 100 + pos[1], pos)
			break