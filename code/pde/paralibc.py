import numpy as np
def jz(n,m,a,b,c):#n是行数，m是列数，a,b,c是矩阵参数
    nn=m*n
    u=np.zeros([nn,nn])
    for i in range(nn):
        if (i+1)%n>=2 or (i+1)%n==0:
            u[i,i-1]=c
        if (i+1)%n+1<=n and (i+1)%n!=0:
            u[i,i+1]=c
        if i-n>=0:
            u[i,i-n]=b
        if i+n<=nn-1:
            u[i,i+n]=b
        u[i,i]=a
    return u
def f(x,y,t):
    z=np.sin(5*np.pi*t)*np.sin(2*np.pi*x)*np.sin(np.pi*y)
    return z
h0,h1,h2=0.001,0.1,0.1
a,b=0,1
c,d=0,1
e=0
xdate=np.arange(a,b+h1,h1)
print(xdate)
ydate=np.arange(c,d+h2,h2)
(n,)=xdate.shape
(m,)=ydate.shape
u_0yt=np.zeros([m])
u_1yt=np.zeros([m])
u_x0t=np.zeros([n])
u_x1t=np.zeros([n])
A=jz(m-2,n-2,-4,1,1)
x_0,y_0=np.meshgrid(xdate[1:-1],ydate[1:-1])
def js(t0):
    t=np.arange(e,t0+h0,h0)
    l=(m-2)*(n-2)
    u=np.zeros(l)
    b=f(x_0,y_0,0)
    b=b.T
    b=b.flatten()
    A1=(h0/(h1**2))*A+np.identity(l)
    for t1 in t[1:]:
        u=np.matmul(A1,u)+h0*b
        b=f(x_0,y_0,t1)
        b=b.T
        b=b.flatten()
        if t1==0.1:
            print(u)
    return u
print(js(1))










