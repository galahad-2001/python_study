# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt

i = 0
k = float(0)
l = float(10000000)
r = float(0.5)
xx = []
yy = []

while i < l:
	x = random.random()
	y = random.random()
	j = ((x-r)**2+(y-r)**2)**0.5
	if j <= r:
		xx.append(x)
		yy.append(y)
		k += 1
	i += 1

print k/(l*r**2)
plot = plt.plot(xx, yy, 'b,')
plt.show()
