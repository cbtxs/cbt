import numpy as np
import copy

def jacobi(A,b):
    (n,)=b.shape
    A=A.astype(float)
    b=b.astype(float)
    nor=np.linalg.norm(A,ord=2)
    er=1
    y=copy.deepcopy(b)
    x=np.zeros(n)+2
    k=0
    while er>1e-10 and k<100:
        k+=1
        for i in range(n):
            i_s=np.delete(np.arange(n),i)
            for j in i_s:
                y[i]=y[i]-A[i,j]*x[j]
            y[i]=y[i]/A[i,i]
        er=np.linalg.norm(x-y,ord=2)
        x=copy.deepcopy(y)
        y=copy.deepcopy(b)
    return x






