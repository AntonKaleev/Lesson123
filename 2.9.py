import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7,4))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-4, 4, 0.1)
y = np.arange(-4, 4, 0.1)
xgrid, ygrid = np.meshgrid(x,y)

zgrid = np.sin(xgrid**2+ygrid**2)/(xgrid**2+ygrid**2)

ax_3d.plot_surface(xgrid, ygrid, zgrid)

plt.show()