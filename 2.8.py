import math

import numpy as np
A = input("Введите координаты атома: ").split()

R = int(input("Введите расстояние: "))

r = math.sqrt(float(A[0])**2+float(A[1])**2+float(A[2])**2)
i = 0

total = 0

vecs = np.array(
[[1.0, 0.0, 2.0],
[-1.0, 0.5, 2.0],
[-2.0, 1.5, 0.0],
[2.5, -1.2, -0.5],
[1.5, 0.2, -0.2]])

len1 = len(vecs)

for i in range(len1):
    r1 = math.sqrt(float(vecs[i, 0])**2 + float(vecs[i, 1])**2 + float(vecs[i, 2])**2)
    if r+R > r1:
        i += 1
        total += 1
print(total)