import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
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
def g(x,y,t):
    z=np.sin(np.pi*x)*np.cos(np.pi*y)*np.exp(-np.pi**2*t/8)
    return z
def f(x,y):
    z=np.sin(np.pi*x)*np.cos(np.pi*y)
    return z
h0,h1,h2=0.01,0.1,0.1
a,b=0,1
c,d=0,1
e=0
xdate=np.arange(a,b+h1,h1)
ydate=np.arange(c,d+h2,h2)
(n,)=xdate.shape
(m,)=ydate.shape
u_0yt=np.zeros([m])
u_1yt=np.zeros([m])
u_x0t=np.zeros([n])
u_x1t=np.zeros([n])
l=(m-2)*(n-2)
A=jz(m-2,n-2,-4,1,1)
for i in range(l):
    if (i+1)%(m-2)<=1:
        A[i,i]+=1
x_0,y_0=np.meshgrid(xdate[1:-1],ydate[1:-1])
def js(t0):
    t=np.arange(e,t0+h0,h0)
    u=f(x_0,y_0)
    u=u.T
    u=u.flatten()
    A1=(h0/(4*(h1**2)))*A+np.identity(l)
    aa=np.linalg.norm(A1,ord=2)
    #A1=(1/aa)*A1
    er=np.array([0])
    for t1 in t[1:]:
        b=np.zeros([m-2,n-2])
        #b[:,0]=g(xdate[1:-1],0,t1-h0)
        #b[:,-1]=g(xdate[1:-1],-1,t1-h0)
        b=b.flatten()
        u=np.matmul(A1,u)+(h0/(4*(h1**2)))*b
        v=g(x_0,y_0,t1)
        v=v.T
        v=v.flatten()
        tmp=max(abs(u/v))
        er=np.append(er,tmp)
    u=u.reshape(m-2,n-2)
    return u.T,er,t
uu,er,tdate=js(12)
plt.plot(tdate,er)
plt.show()

