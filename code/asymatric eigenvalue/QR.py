import numpy as np
import copy
import time

star=time.time()
def givens(x,y):
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
def QR(a):
    a=a.astype(float)
    (m,n)=a.shape
    q=np.identity(m)
    for i in range(n):
        for j in range(m)[i+1:]:
            G=givens(a[i,i],a[j,i])
            a[[i,j],i:]=np.matmul(G,a[[i,j],i:])
            q[:,[i,j]]=np.matmul(q[:,[i,j]],G.T)
    return q,a
def givenstrun(G,A,i,j): 
    tmp1=np.matmul(G[0,:],A[[i,j]])
    tmp2=np.matmul(G[1,:],A[[i,j]])
    A[i,:]=copy.deepcopy(tmp1)
    A[j,:]=copy.deepcopy(tmp2)
    tmp1=np.matmul(G[0,:],A.T[[i,j]])
    tmp2=np.matmul(G[1,:],A.T[[i,j]])
    A[:,i]=copy.deepcopy(tmp1)
    A[:,j]=copy.deepcopy(tmp2)
    return A
def eigenvalue(x):
    A=x.astype(float)
    (n,n)=A.shape
    #将A化为上Hessenberg矩阵
    for i in range(n-2):
        for j in range(n)[i+2:]:
            G=givens(A[i+1,i],A[j,i])
            A=givenstrun(G,A,i+1,j)
    err1=np.arange(n).astype(float)
    err2=np.zeros(n)
    er=np.linalg.norm(err1-err2,ord=2)
    lam,k=0,0
    while er>1e-10:
        k+=1
        if k>100:
            lam+=A[-1,-1]
            A=A-A[-1,-1]*np.eye(n)
        G=np.array([[A[0,0],A[1,0]],[-A[1,0],A[0,0]]])/np.linalg.norm(A[:,0],ord=2)
        A=givenstrun(G,A,0,1)
        for i in range(n-2):
            G=givens(A[i+1,i],A[i+2,i])
            A=givenstrun(G,A,i+1,i+2)
        err2=copy.deepcopy(err1)
        err1=copy.deepcopy(A.diagonal())
        er=np.linalg.norm(err1-err2,ord=2)/n
    err1+=lam
    print(k)
    return err1
x=np.diag([1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9])
np.random.seed(0)
T=10*np.random.random(size=(9,9))
t=np.linalg.inv(T)
y=np.matmul(T,x)
z=np.matmul(y,t)
zz=eigenvalue(z)
print(zz)
end=time.time()
print(end-star)

