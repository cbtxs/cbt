import numpy as np
import copy
import time
start=time.time()
def GS(A,b):
    (n,n)=A.shape
    A=A.astype(float)
    b=b.astype(float)
    y=copy.deepcopy(b)
    x=np.zeros(n)
    x[5]=12
    er=1
    while er>1e-10:
        for i in range(n):
            for j in range(n):
                if j<i:
                    y[i]-=A[i,j]*y[j]
                elif j>i:
                    y[i]-=A[i,j]*x[j]
            y[i]/=A[i,i]
        er=np.linalg.norm(x-y,ord=2)
        x=copy.deepcopy(y)
        y=copy.deepcopy(b)
    return x


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







aa=np.arange((n+1)**2)
bb=np.sum(A,axis=1)
print(bb)
print(GS(A,bb))
end=time.time()
print(end-start)




