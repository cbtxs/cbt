import numpy as np
import copy
import time

star=time.time()
def GTAG(G,A,i,j):
    tmp1=np.matmul(G[0,:],A[[i,j]])
    tmp2=np.matmul(G[1,:],A[[i,j]])
    A[i,:]=copy.deepcopy(tmp1)
    A[j,:]=copy.deepcopy(tmp2)
    tmp1=np.matmul(G[0,:],A.T[[i,j]])
    tmp2=np.matmul(G[1,:],A.T[[i,j]])
    A[:,i]=copy.deepcopy(tmp1)
    A[:,j]=copy.deepcopy(tmp2)
    return A
def jacobitrun(A):
    (n,n)=A.shape
    off=1
    while off>1e-10:
        B=copy.deepcopy(A)
        for i in range(n):
            B[i,i]=0
        B=abs(B)
        y=np.where(B==np.max(B))
        i,j=y[0][0],y[1][0]
        tau=(A[i,i]-A[j,j])/(2*A[i,j])
        t=np.sign(tau)/(abs(tau)+np.sqrt(1+tau**2))
        c=1/(np.sqrt(1+t**2))
        s=c*t
        G=np.array([[c,s],[-s,c]])
        A=GTAG(G,A,i,j)
        off=sum(sum(B))
    return A.diagonal()
x=np.diag([0.1,99.2,99.3,99.4,99.5,99.6,99.7,99.8,99.9])
np.random.seed(0)
T=10*np.random.random(size=(9,9))
t,fnbdjv=np.linalg.qr(T)
y=np.matmul(t,x)
z=np.matmul(y,t.T)
zz=jacobitrun(z)
print(zz)
end=time.time()
print(end-star)






























