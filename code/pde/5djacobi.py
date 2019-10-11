import numpy as np
import copy
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
m0=1/(2/(h1**2)+2/(h2**2))
m1=m0/(h1**2)
m2=m0/(h2**2)
xdate=np.linspace(a,b,n+1)
ydate=np.linspace(c,d,n+1)
x_0,y_0=np.meshgrid(xdate,ydate)
u1=np.zeros([n+1,n+1])
u0=copy.deepcopy(u1)
b=f(x_0,y_0)
er,k=1,1
while er>1e-10:
    k+=1
    for i in range(n+1)[1:-1]:
        for j in range(n+1)[1:-1]:
            u1[i,j]=m2*(u0[i-1,j]+u0[i+1,j])+m1*(u0[i,j+1]+u0[i,j-1])-b[i,j]*m0
    u1[:,0]=copy.deepcopy(u1[:,1])
    u1[:,-1]=copy.deepcopy(u1[:,-2])
    er=abs(u0-u1).max()
    u0=copy.deepcopy(u1)
print(u0)
kkk=zj(x_0,y_0)
er=np.linalg.norm(u0[1:-1,1:-1]-kkk[1:-1,1:-1],ord=2)/(n-1)**2
err=abs(u0[1:-1,1:-1]-kkk[1:-1,1:-1]).max()
print(kkk)
print(er)
print(err)
print(k)


















