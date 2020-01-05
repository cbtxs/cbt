import numpy as np
import copy
def pos_eig(A):
    (n,n) = A.shape
    x0 = np.zeros(n)+1
    u0, u1 = 0, 10000
    while abs(u0-u1)>1e-15:
        u0 = copy.deepcopy(u1)
        x0 = np.einsum('ij,j->i', A, x0)
        x0 = x0/(np.einsum('i,i',x0,x0))**(1/2)
        u1 = np.einsum('j,ji,i', x0,A,x0)
    return u1, x0

def pes_eig(A):
    (n,n) = A.shape
    x0 = np.zeros(n)+1
    u0, u1 = 0, 10000
    k=0
    while abs(u0-u1)>1e-15:
        u0 = copy.deepcopy(u1)
        x0 = np.linalg.solve(A,x0)
        x0 = x0/(np.einsum('i,i',x0,x0))**(1/2)
        u1 = np.einsum('j,ji,i', x0,A,x0)
        k+=1
    return u1,x0, k
A = np.zeros(10000,10000)

A = np.array([[-5,-10,-20],[-10,10,30],[-20,30,100]])
#A = np.diag([1,4,5])
print(pos_eig(A), pes_eig(A))
print(np.linalg.eig(A))


