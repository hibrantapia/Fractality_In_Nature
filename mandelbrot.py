import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, z=0, n=0):
    if n > 100:
        return n
    if abs(z) > 2:
        return n
    else:
        return mandelbrot(c, z**2 + c, n+1)

#plot the mandelbrot set
def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + Y*1j
    Z = np.frompyfunc(mandelbrot, 1, 1)(C).astype(float)
    plt.imshow(Z, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.show()

plot_mandelbrot(-2, 1, -1, 1, 500, 500)