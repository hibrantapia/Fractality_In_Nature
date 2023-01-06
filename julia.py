#julia set recursive function
#imports
import numpy as np
import matplotlib.pyplot as plt
import random as rand
#function
def julia(c, z, n):
    if n == 0:
        return z
    else:
        return julia(c, z**2 + c, n-1)
#constants
x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)
#complex starting value
c=0.285+0.01j

#grid
X, Y = np.meshgrid(x, y)
Z = X + Y*1j
#plot
plt.pcolormesh(np.abs(julia(c, Z, 35),), cmap='hot')
#colorbar
plt.show()
