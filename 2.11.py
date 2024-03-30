
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7,4))
ax_3d = fig.add_subplot(projection='3d')

r = 10
phi = np.arange(0,2*np.pi,40)
theta = np.arange(-40,2*np.pi,40)

R = np.linspace(-40,r,40)


phigrid, thetagrid = np.meshgrid(phi,theta)

xgrid = (R+r*np.cos(phigrid))*np.cos(thetagrid)
ygrid = (R+r*np.sin(phigrid))*np.sin(thetagrid)
zgrid = r*np.sin(phigrid)

ax_3d.plot_surface(xgrid, ygrid, zgrid)

plt.show()