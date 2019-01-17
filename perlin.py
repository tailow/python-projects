import opensimplex
from matplotlib import pyplot as plt

values = []

width = 200
height = 200
scale = 1

noise = opensimplex.OpenSimplex()

for y in range(height):
    values.append([])
    for x in range(width):
        values[y].append(noise.noise2d(x / width * scale, y / height * scale))

plt.pcolor(values, cmap="PuBu")
plt.show()
