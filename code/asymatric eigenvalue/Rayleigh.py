'''
Rayleigh商迭代求矩阵特征值特征向量

作者：陈春雨
date：2019-9-3
'''

import numpy as np
import copy

#Rayleigh商迭代
def Rayleigh(A):
    A = A.astype(float)
    (n,n) = A.shape
    x0 = np.array([3/np.sqrt(10),0.01,0])
    k = 0
    E = np.identity(n)
    l1,l2 = 0,1
    t = np.dot(x0, np.matmul(A, x0))
    while abs(l1-l2)>1e-15:
        y0 = np.linalg.solve(A - t*E, x0)
        x0 = y0/(np.einsum('i,i',y0,y0))**(1/2)
        l2 = copy.deepcopy(l1)
        l1 = np.einsum('i,ij,j',x0,A,x0)
        k += 1
    return x0, t, k
#测试

aa=np.array([[1,0,2],[0,2,0],[0,4,-1]])
l,n, j=Rayleigh(aa)
print(l,n,j)
print(np.linalg.eig(aa))



















