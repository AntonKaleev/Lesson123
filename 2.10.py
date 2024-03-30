import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2, 8, 60)
y = np.linspace(0, 5, 50)
def func(x, y):
 return (1/4)*np.sin((1/2)*x**2-y)-np.e**(-(x-5)**2+(y-2)**2)

X, Y = np.meshgrid(x, y)
Z = func(X, Y)


fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(Z)

plt.show()