import numpy as np

def f(x,y):
    z=np.sin(np.pi*x)*np.cos(np.pi*y)
    return z
def g(x,y,t):
    z=np.sin(np.pi*x)*np.cos(np.pi*y)*np.exp(-t*np.pi*np.pi/8)
    return z
n=int(input('n='))
h0,h1=0.1/n,1/n
tmx=1
xdate=np.linspace(0,1,n+1)
ydate=np.linspace(0,1,n+1)
tdate=np.arange(0,tmx,h0)
A1=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1):
    if i==0:
        for j in range(n+1):
            A1[j,j]=1
    elif i==n:
        for j in range(n+1):
            A1[i*(n+1)+j,i*(n+1)+j]=1
    else:
        A1[i*(n+1),i*(n+1)]=1
        A1[i*(n+1),i*(n+1)+1]=-1
        A1[(i+1)*(n+1)-1,(i+1)*(n+1)-1]=1
        A1[(i+1)*(n+1)-1,(i+1)*(n+1)-2]=-1
        for j in range(n+1)[1:-1]:
            A1[i*(n+1)+j,i*(n+1)+j]=1+h0/(16*h1**2)
            A1[i*(n+1)+j,(i+1)*(n+1)+j]=-h0/(32*h1**2)
            A1[i*(n+1)+j,(i-1)*(n+1)+j]=-h0/(32*h1**2)
B1=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1)[1:-1]:
    for j in range(n+1)[1:-1]:
        B1[i*(n+1)+j,i*(n+1)+j]=1-h0/(16*h1**2)
        B1[i*(n+1)+j,i*(n+1)+j-1]=h0/(32*h1**2)
        B1[i*(n+1)+j,i*(n+1)+j+1]=h0/(32*h1**2)
A2=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1):
    if i==0:
        for j in range(n+1):
            A2[j,j]=1
    elif i==n:
        for j in range(n+1):
            A2[i*(n+1)+j,i*(n+1)+j]=1
    else:
        A2[i*(n+1),i*(n+1)]=1
        A2[i*(n+1),i*(n+1)+1]=-1
        A2[(i+1)*(n+1)-1,(i+1)*(n+1)-1]=1
        A2[(i+1)*(n+1)-1,(i+1)*(n+1)-2]=-1
        for j in range(n+1)[1:-1]:
            A2[i*(n+1)+j,i*(n+1)+j]=1+h0/(16*h1**2)
            A2[i*(n+1)+j,i*(n+1)+j+1]=-h0/(32*h1**2)
            A2[i*(n+1)+j,i*(n+1)+j-1]=-h0/(32*h1**2)
B2=np.zeros([(n+1)**2,(n+1)**2])
for i in range(n+1)[1:-1]:
    for j in range(n+1)[1:-1]:
        B2[i*(n+1)+j,i*(n+1)+j]=1-h0/(16*h1**2)
        B2[i*(n+1)+j,(i+1)*(n+1)+j]=h0/(32*h1**2)
        B2[i*(n+1)+j,(i-1)*(n+1)+j]=h0/(32*h1**2)
xx,yy=np.meshgrid(xdate,ydate)
u=f(xx,yy)
u=(u.T).flatten()
for t in tdate[1:]:
    tmp=np.linalg.solve(A1,np.matmul(B1,u))
    u=np.linalg.solve(A2,np.matmul(B2,tmp))
u_true=g(xx,yy,tmx)
u=u.reshape(n+1,n+1)
er=abs(u_true[1:-1,1:-1]-u.T[1:-1,1:-1]).max()
print(er)



