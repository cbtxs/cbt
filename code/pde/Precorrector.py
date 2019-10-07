import numpy as np
import copy
def f(x,y):
    z=np.sin(np.pi*x)*np.cos(np.pi*y)
    return z
def g(x,y,t):
    z=np.sin(np.pi*x)*np.cos(np.pi*y)*np.exp(-t*np.pi*np.pi/8)
    return z
n=int(input('n='))
h0,h1=1/n,1/n
tmx=1
xdate=np.linspace(0,1,n+1)
ydate=np.linspace(0,1,n+1)
tdate=np.arange(0,tmx+h0,h0)
m=tdate.shape
A=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1):
    for j in range(n+1):
        if i==0 or i==n:
            A[i*(n+1)+j,i*(n+1)+j]=1
        elif j==0:
            A[i*(n+1)+j,i*(n+1)+j]=1
            A[i*(n+1)+j,i*(n+1)+j+1]=-1
        elif j==n:
            A[i*(n+1)+j,i*(n+1)+j]=1
            A[i*(n+1)+j,i*(n+1)+j-1]=-1
        else:
            A[i*(n+1)+j,i*(n+1)+j]=1+h0/(16*h1**2)
            A[i*(n+1)+j,i*(n+1)+j-1]=-h0/(32*h1**2)
            A[i*(n+1)+j,i*(n+1)+j+1]=-h0/(32*h1**2)
B=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1):
    for j in range(n+1):
        if i==0 or i==n:
            B[i*(n+1)+j,i*(n+1)+j]=1
        elif j==0:
            B[i*(n+1)+j,i*(n+1)+j]=1
            B[i*(n+1)+j,i*(n+1)+j+1]=-1
        elif j==n:
            B[i*(n+1)+j,i*(n+1)+j]=1
            B[i*(n+1)+j,i*(n+1)+j-1]=-1
        else:
            B[i*(n+1)+j,i*(n+1)+j]=1+h0/(16*h1**2)
            B[i*(n+1)+j,(i+1)*(n+1)+j]=-h0/(32*h1**2)
            B[i*(n+1)+j,(i-1)*(n+1)+j]=-h0/(32*h1**2)
P=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1)[1:-1]:
    for j in range(n+1)[1:-1]:
        P[i*(n+1)+j,i*(n+1)+j]=-h0/(4*h1**2)
        P[i*(n+1)+j,(i+1)*(n+1)+j]=h0/(16*h1**2)
        P[i*(n+1)+j,(i-1)*(n+1)+j]=h0/(16*h1**2)
        P[i*(n+1)+j,i*(n+1)+j-1]=h0/(16*h1**2)
        P[i*(n+1)+j,i*(n+1)+j+1]=h0/(16*h1**2)
A=np.array([B,A])
u=np.zeros([m[0],(n+1)**2])
x_d,y_d=np.meshgrid(xdate,ydate)
u[0,:]=(f(x_d,y_d)).T.flatten()
for i in range(m[0])[1:]:
    u[i,:]=copy.deepcopy(u[i-1,:])
    for j in range(2):
        tmp=copy.deepcopy(u[i,:])
        tmp=tmp.reshape(n+1,n+1)
        tmp[:,0]=0
        tmp[:,-1]=0
        tmp=tmp.flatten()
        u[i,:]=np.linalg.solve(A[j],tmp)
    u[i,:]=np.matmul(P,u[i,:])+u[i-1,:]
    for k in range(n+1):
        u[i,:][k*(n+1)]=u[i,:][k*(n+1)+1]
        u[i,:][k*(n+1)+n]=u[i,:][k*(n+1)+n-1]
u_ture=g(x_d,y_d,tmx)
u_s=(u[-1,:].reshape(n+1,n+1)).T
er=abs(u_s/u_ture)
print(u_s)
print(u_ture)
print(er)


















