import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
import copy

#############高斯选主元###########
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

##########向后差分########

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
h0,h1,h2=0.0025,0.025,0.025
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
print(A)
def js(t0):
    t=np.arange(e,t0+h0,h0)
    u=f(x_0,y_0)
    u=u.T
    u=u.flatten()
    A1=(h0/(4*(h1**2)))*A-np.identity(l)
    er=np.array([0])
    for t1 in t[1:]:
        b=np.zeros([m-2,n-2])
        #b[:,0]=g(xdate[1:-1],0,t1-h0)
        #b[:,-1]=g(xdate[1:-1],-1,t1-h0)
        b=b.flatten()
        b=-u-h0*b
        u=gauss(A1,b)
        v=g(x_0,y_0,t1)
        v=v.T
        v=v.flatten()
        tmp=np.linalg.norm(u-v,ord=2)/(n-2)**2
        er=np.append(er,tmp)
    return u.T/v.T,er,t
uu,er,tdate=js(0.1)
print(er)
plt.plot(tdate,er)
plt.show()

