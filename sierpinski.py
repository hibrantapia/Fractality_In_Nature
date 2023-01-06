#graph using pcolormesh a 1d representation of sierpinski triangle in conway's game of life
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
tiempos = 600
casillas = np.zeros((600,301))
y = 300
casillas[0,150]=1
for i in range(0,tiempos-1,1):
    for j in range(0,y-1,1):
        if casillas[i,j-1] == 1 and casillas[i,j+1] == 1:
            casillas[i+1,j] = 0
        elif casillas[i,j-1] == 0 and casillas[i,j+1] == 0:
            casillas[i+1,j] = 0
        else:
            casillas[i+1,j] = 1
#transpose the array
casillas = casillas.T
plt.pcolormesh(casillas)
#axis labels
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()

#same as above but with a different initial condition
# casillas2=np.zeros((600,301))
# for i in range(0,tiempos-1,1):
#     for j in range(0,y-1,1):
#         casillas2[i,j]=rnd.randint(0,1) 

# for i in range(0,tiempos-1,1):
#     for j in range(0,y-1,1):
#         if casillas2[i,j-1] == 1 and casillas2[i,j+1] == 1:
#             casillas2[i+1,j] = 0
#         elif casillas2[i,j-1] == 0 and casillas2[i,j+1] == 0:
#             casillas2[i+1,j] = 0
#         else:
#             casillas2[i+1,j] = 1
# plt.pcolormesh(casillas2.T)
# plt.show()