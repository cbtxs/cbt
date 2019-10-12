import numpy as np
import copy 
import time
start=time.time()
def CG(A,b):
    A=A.astype(float)
    b=b.astype(float)
    (n,n)=A.shape
    x0=np.zeros(n)+2
    r0=b-np.matmul(A,x0)
    bate=np.linalg.norm(r0,ord=2)
    p1=copy.deepcopy(r0)
    for i in range(n)[1:]:
        pa=np.matmul(A,p1)
        yl=np.dot(r0,r0)/np.dot(p1,pa)
        x0=x0+yl*p1
        r1=copy.deepcopy(r0)
        r0=r0-yl*pa
        p1=r0+np.dot(r0,r0)/np.dot(r1,r1)*p1
        rels=np.linalg.norm(r0,ord=2)/bate
        if rels<1e-10:
            break
    if rels<1e-10:
        return x0
    else:
        return 'failed'




n=int(input('n='))
a,b=0,np.pi
c,d=0,1
h1=(b-a)/n
h2=(d-c)/n
xdate=np.linspace(a,b,n+1)
ydate=np.linspace(c,d,n+1)
A=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1):
    if i==0:
        for j in range(n+1):
            A[j,j]=1
    elif i==n:
        for j in range(n+1):
            A[n*(n+1)+j,n*(n+1)+j]=1
    else:
        A[i*(n+1),i*(n+1)]=1
        A[(i+1)*(n+1)-1,(i+1)*(n+1)-1]=1
        for j in range(n+1)[1:-1]:
            A[i*(n+1)+j,i*(n+1)+j]=-2/h1**2-2/h2**2
            A[i*(n+1)+j,i*(n+1)+j-1]=1/h2**2
            A[i*(n+1)+j,i*(n+1)+j+1]=1/h2**2
            A[i*(n+1)+j,(i-1)*(n+1)+j]=1/h1**2
            A[i*(n+1)+j,(i+1)*(n+1)+j]=1/h1**2
A=A.T+A        
bb=np.sum(A,axis=1)
print(CG(A,bb))
end=time.time()
print(end-start)

























