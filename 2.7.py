import numpy as np
A = np.array([10, 500, 27, 88, 367, 57, 88])

C = np.array(A)

A.sort()

min1 = np.argwhere(C == A[0])
min2 = np.argwhere(C == A[1])
min3 = np.argwhere(C == A[2])



print(min1,min2,min3)