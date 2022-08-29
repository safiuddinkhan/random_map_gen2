import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]


for y in range(ypix):
	for x in range(xpix):
		print("[%d %d]: %f" % (y,x,pic[x][y]))

plt.imshow(pic, cmap='gray')
plt.imsave("test1.png",pic)
plt.show()
