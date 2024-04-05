import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

dx = 0.001
x = np.arange(-4, 4, dx)
f0 = lambda x: x**2*(x-4)**2*np.exp(-x**2)*(-1)
plt.plot(x, f0(x))
plt.show()

from scipy.optimize import minimize
result = minimize(f0, x0=1)
print(result)


(x+y)**2-2*x*(y+a)-2*y*b+a+b