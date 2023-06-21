from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# a= np.array([1,2,3])
# b= np.array([4,5,6,7])
a=np.arange(-4,4,0.2)
b=a
a,b= np.meshgrid(a,b)
# print(a)
# print(b)

fig= plt.figure()
axes= fig.add_subplot(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow')
plt.show()

fig= plt.figure()
axes= fig.add_subplot(projection='3d')
axes.contour(a,b,a**2+b**2,cmap='rainbow')
plt.title("Contour Plot")
plt.show()