import numpy as np
import copy
import time
start=time.time()
def givens(a,b):
    x=copy.deepcopy(a)
    y=copy.deepcopy(b)
    if y==0:
        if x>=0:
            c,s=1,0
        else:
            c,s=-1,0
    else:
        if abs(y)>abs(x):
            tmp=x/y
            s=np.sign(y)/(np.sqrt(1+tmp**2))
            c=s*tmp
        else:
            tmp=y/x
            c=np.sign(x)/(np.sqrt(1+tmp**2))
            s=c*tmp
    z=np.array([[c,s],[-s,c]])
    return z
def GM(A,b):
    (n,n)=A.shape
    x0=np.zeros(n)+3
    r0=b-np.matmul(A,x0)
    bate=np.linalg.norm(r0,ord=2)
    itermax=n
    v=r0/bate
    H=np.zeros([itermax+1,itermax+1])
    ylon=np.zeros(n+1)
    ylon[0]=bate
    for i in range(itermax):
        om=np.matmul(A,v[i].T)
        for j in range(i+1):
            H[j,i]=np.dot(v[j],om)
            om-=H[j,i]*v[j].T
        H[i+1,i]=np.linalg.norm(om,ord=2)
        v=np.vstack((v,om.T/H[i+1,i]))
        for k in range(i):
            H[k:k+2,i]=np.matmul(Q[k],H[k:k+2,i])
        G=givens(H[i,i],H[i+1,i])
        H[i:i+2,i]=np.matmul(G,H[i:i+2,i])
        ylon[i:i+2]=np.matmul(G,ylon[i:i+2])
        if i==0:
            Q=np.array([G])
        else:
            G=np.array([G])
            Q=np.concatenate((Q,G),axis=0)
        re=abs(ylon[i+1]/bate)
        if re<1e-10:
            break
        print(i)
    m=i
    y_m=np.matmul(np.linalg.inv(H[0:m+1,0:m+1]),ylon[0:m+1])
    x_m=np.matmul(v[:-1].T,y_m)+x0
    if re<1e-10:
        return x_m
    else :
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
bb=np.array([np.sum(A,axis=1)])
print(GM(A,bb))
end=time.time()
print(end-start)
