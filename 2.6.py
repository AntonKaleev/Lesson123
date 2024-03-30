import numpy as np
A = np.array([[0, 0, 1],[0, 0, 0], [0, 0, 0]])
def nonzero(A):
    number = np.argwhere(A != 0)
    print(number)
nonzero(A)