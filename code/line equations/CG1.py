import numpy as np
import copy
import time
def CG(A,b):
    (n,n)=A.shape
    x0=np.zeros(n)+1
    r0=b-np.matmul(A,x0)
    bate=np.linalg.norm(r0,ord=2)
    for i in range(n+1):
        ro=np.einsum('i,i->',r0,r0)
        if i>1:
            mu=ro/ro0
            pm=r0+mu*pm
        else:
            pm=copy.deepcopy(r0)
        qm=np.matmul(A,pm)
        yl=ro/np.einsum('i,i->',pm,qm)
        x0=x0+yl*pm
        r1=copy.deepcopy(r0)
        r0=r0-yl*qm
        rels=np.linalg.norm(r0,ord=2)/bate
        if rels<1e-10:
            break
        ro0=copy.deepcopy(ro)
    if rels<1e-10:
        return x0
    else:
        return x0
start = time.time()
A=np.array([[6,3],[3,2]])
b=np.array([0,-1])
print(CG(A,b))
end=time.time()
print(end-start)


