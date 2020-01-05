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
    v=np.array([v])
    H=np.zeros([itermax+1,itermax+1])
    ylon=np.zeros(n+1)
    ylon[0]=bate
    for i in range(itermax):
        om=np.einsum('ij,j->i',A,v[i])
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
    m=i
    y_m=np.matmul(np.linalg.inv(H[0:m+1,0:m+1]),ylon[0:m+1])
    x_m=np.matmul(v[:-1].T,y_m)+x0
    if re<1e-10:
        return x_m
    else :
        return 'failed'


A = np.array([[0, 1, 0,0,0 ],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[1,2,3,4,0]])
b=np.array([1,0,0,0,0])
print(GM(A,b))
end=time.time()
print(end-start)


