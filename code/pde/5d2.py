import numpy as np
import copy
import scipy.linalg
def f(x,y):
    z=np.cos(3*x)*np.sin(np.pi*y)
    return -z
#真解
def zj(x,y):
    z=np.cos(3*x)*np.sin(np.pi*y)/(9+np.pi**2)
    return z

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
            A[j,j+n+1]=-1
    elif i==n:
        for j in range(n+1):
            A[n*(n+1)+j,(n-1)*(n+1)+j]=-1
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

x_0,y_0=np.meshgrid(xdate[1:-1],ydate[1:-1])
F=np.zeros([n+1,n+1])
F[1:-1,1:-1]=f(x_0,y_0)
F=F.T
F=F.flatten()
u=np.linalg.solve(A,F)
u=u.reshape(n+1,n+1)
x_1,y_1=np.meshgrid(xdate,ydate)
kkk=zj(x_1,y_1)
er=abs(u[1:-1,1:-1]-kkk.T[1:-1,1:-1]).max()
err=np.linalg.norm(u[1:-1,1:-1]-kkk.T[1:-1,1:-1],ord=1)/(n-1)**2
print(u)
print(kkk.T)
print(abs(u-kkk.T))
print('***',er)
print(err)






























