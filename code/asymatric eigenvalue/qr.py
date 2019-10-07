import numpy as np
import copy

def house(x):
    xg=0
    for x1 in x[1:]:
        xg+=x1**2
    if xg==0:
        if x[0]<0:
            x[0]*=2
            beta=2/(x[0]**2)
        else:
            x[0]=0
            beta=0
    else:
        al=np.sqrt(x[0]**2+xg)
        if x[0]<0:
            x[0]=x[0]-al
        else:
            x[0]=-xg/(x[0]+al)
        beta=2/(x[0]**2+xg)
    return x,beta
def qr(A):
    A=A.astype(float)
    (n,n)=A.shape
    for i in range(n-2):
        y=copy.deepcopy(A[i+1:,i])
        v,bate=house(y)
        v=np.array([v])
        tmp=np.matmul(v,A[i+1:,i:])
        A[i+1:,i:]=A[i+1:,i:]-bate*np.matmul(v.T,tmp)
        tmp=np.matmul(v,A.T[i+1:,i:])
        A[i:,i+1:]=A[i:,i+1:]-bate*np.matmul(v.T,tmp).T
    return A
x=np.diag([0.1,99.2,99.3,99.4,99.5,99.6,99.7,99.8,99.9])
np.random.seed(0)
T=10*np.random.random(size=(9,9))
t,fnbdjv=np.linalg.qr(T)
y=np.matmul(t,x)
z=np.matmul(y,t.T)
zz=qr(z)
print(zz)








