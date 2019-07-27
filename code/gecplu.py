import numpy as np
import copy

#LU分解
def gecplu(x):
    (n,n)=x.shape
    l=np.identity(n)
    p=np.arange(n)
    u=x.astype(float)
    for i in range(n-1):
        k=np.argmax(abs(u[i:,i]))
        k=k+i
        if i!=k:
            tmp=copy.deepcopy(u[i,:])
            u[i,:]=copy.deepcopy(u[k,:])
            u[k,:]=copy.deepcopy(tmp)
            tmmp=copy.deepcopy(p[i])
            p[i]=copy.deepcopy(p[k])
            p[k]=copy.deepcopy(tmmp)
        for j in range(n)[i+1:]:
            u[j,i]=u[j,i]/u[i,i]
            u[j,i+1:]=u[j,i+1:]-u[j,i]*u[i,i+1:]
    for i in range(n):
        for j in range(i):
            l[i,j]=u[i,j]
            u[i,j]=0
    return l,u,p


def gauss(A,b):           #要求b为一位数组np.array([])型的
    (n,n)=A.shape
    (l,u,p)=gecplu(A)
    tmp=copy.deepcopy(b)
    for i in range(n):
        b[i]=copy.deepcopy(tmp[p[i]])
    #计算ly=b
    y=b.astype(float)
    for i in range(n)[1:]:
        for j in range(n)[:i]:
            y[i]=y[i]-l[i,j]*y[j]
    x=b.astype(float)
    #计算ux=y
    for i in range(n):
        i=n-i-1
        for j in range(n)[i+1:]:
            y[i]=y[i]-u[i,j]*x[j]
        x[i]=y[i]/u[i,i]
    return x

aa=np.array([[3.8,4.6,5.443,6.882],
    [8.674,9.423,10.255,6582.5666],
    [6.44,8.87,28.4,3.39],
    [20.65,43456.499,45.62,69.02]])
bb=np.sum(aa,axis=1)
print(gauss(aa,bb))

