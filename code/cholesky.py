import numpy as np

def choleskyf(x):
    x=x.astype(float)
    (n,n)=x.shape
    lf=np.zeros([n,n])
    for i in range(n):
        for j in range(i):
            x[i,i]=x[i,i]-lf[i,j]**2
        lf[i,i]=np.sqrt(x[i,i])
        for j in range(n)[i+1:]:
            for k in range(i):
                x[i,j]=x[i,j]-lf[i,k]*lf[j,k]
            lf[j,i]=x[i,j]/lf[i,i]
    return lf
def cholesky(A,b):        #要求b为一位数组np.array([])型的
    l=choleskyf(A)
    u=np.transpose(l)
    (n,n)=A.shape
    #计算ly=b
    b=b.astype(float)
    y=b.astype(float)
    for i in range(n):
        for j in range(n)[:i]:
            b[i]=b[i]-l[i,j]*y[j]
        y[i]=b[i]/l[i,i]
    x=b.astype(float)
     #计算ux=y
    for i in range(n):
        i=n-i-1
        for j in range(n)[i+1:]:
            y[i]=y[i]-u[i,j]*x[j]
        x[i]=y[i]/u[i,i]
    return x
aa=np.array([[5,2,-4,0],
    [2,1,-2,0],
    [-4,-2,5,0],
    [0,0,0,1]])
bb=np.sum(aa,axis=1)
print(cholesky(aa,bb))
