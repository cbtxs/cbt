import numpy as np

def singular(A):
    v = np.einsum('ik, kj -> ij', A.T, A)
    u = np.einsum('ki, jk -> ij', A.T, A)
    h1 = np.linalg.eig(v)
    h2 = np.linalg.eig(u)
    return h1,h2,v,u
A = np.array([[1, 1, 0, 1], [1, -1, 1, 0], [2, 2, 0, 2]])
print(singular(A)[0][1])
print(singular(A)[1][1])
print(singular(A)[2])
print(singular(A)[3])
