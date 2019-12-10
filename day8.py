'''input
0222112222120000
'''
image = list(input())

WIDTH = 25
HEIGHT = 6

n = WIDTH*HEIGHT
layers = [image[i:i + n] for i in range(0, len(image), n)]

statistics = []
for layer in layers:
	a = layer.count('0')
	b = layer.count('1')
	c = layer.count('2')
	statistics.append((a,b,c))

stat_sorted = sorted(statistics, key=lambda x: x[0])
print(stat_sorted[0])
print(int(stat_sorted[0][1]) * int(stat_sorted[0][2]))

final_image = []
for pixel in range(n):
	top_layter = layers[0]
	val = top_layter[pixel]
	if val == '2':
		for layer in layers[1:]:
			val = layer[pixel]
			if val == '0':
				break
			elif val == '1':
				break
			elif val == '2':
				continue
	final_image.append(val)

print(''.join(final_image))

from PIL import Image
import numpy

img = Image.new('RGB', (WIDTH, HEIGHT))
for x in range(WIDTH):
	for y in range(HEIGHT):
		val = final_image[(y*WIDTH) + x]
		if val == '1':
			img.putpixel((x,y), (255,255,255))
		elif val == '0':
			img.putpixel((x,y), (0,0,0))
img.show()
