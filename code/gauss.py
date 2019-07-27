import numpy as np

#LU分解
def lu(x):
    (n,n)=x.shape
    x=x.astype(float)
    for i in range(n-1):
        for j in range(n)[i+1:]:
            x[j,i]=x[j,i]/x[i,i]
            x[j,i+1:]=x[j,i+1:]-x[j,i]*x[i,i+1:]
    l=np.identity(n)
    for i in range(n):
        for j in range(i):
            l[i,j]=x[i,j]
            x[i,j]=0
    u=x
    return l, u
#计算Ax=b
def gauss(A,b):        #要求b为一位数组np.array([])型的
    (l,u)=lu(A)
    (n,n)=A.shape
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












