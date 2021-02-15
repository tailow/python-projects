import opensimplex
import math
from matplotlib import pyplot as plt

values = []

width = 200
height = 200
scale = 10

noise = opensimplex.OpenSimplex()

for y in range(height):
    values.append([])
    for x in range(width):
        values[y].append(math.floor(5 * math.cos(2 + noise.noise2d(x / width * scale, y / height * scale))))

plt.pcolor(values, cmap="plasma")
plt.show()
