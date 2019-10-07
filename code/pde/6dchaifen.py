import numpy as np

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
A=np.zeros([(n-1)**2,(n-1)**2])
for i in range(n-1):
    for j in range(n-1):
        if j==0: 
            A[i*(n-1)+j,i*(n-1)+j+1]=-h0/(32*h1**2)
            if i<n-2:
                A[i*(n-1)+j,(i+1)*(n-1)+j]=-h0/(32*h1**2)
            if i>0:
                A[i*(n-1)+j,(i-1)*(n-1)+j]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j]=1+3*h0/(32*h1**2)

        elif j==n-2: 
            A[i*(n-1)+j,i*(n-1)+j-1]=-h0/(32*h1**2)
            if i<n-2:
                A[i*(n-1)+j,(i+1)*(n-1)+j]=-h0/(32*h1**2)
            if i>0:
                A[i*(n-1)+j,(i-1)*(n-1)+j]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j]=1+3*h0/(32*h1**2)

        elif i==0 :
            A[i*(n-1)+j,i*(n-1)+j+1]=-h0/(32*h1**2)
            A[i*(n-1)+j,(i+1)*(n-1)+j]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j]=1+h0/(8*h1**2)
            A[i*(n-1)+j,i*(n-1)+j-1]=-h0/(32*h1**2)

        elif i==n-2:
            A[i*(n-1)+j,i*(n-1)+j+1]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j-1]=-h0/(32*h1**2)
            A[i*(n-1)+j,(i-1)*(n-1)+j]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j]=1+h0/(8*h1**2)

        else:
            A[i*(n-1)+j,i*(n-1)+j+1]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j-1]=-h0/(32*h1**2)
            A[i*(n-1)+j,(i+1)*(n-1)+j]=-h0/(32*h1**2)
            A[i*(n-1)+j,(i-1)*(n-1)+j]=-h0/(32*h1**2)
            A[i*(n-1)+j,i*(n-1)+j]=1+h0/(8*h1**2)
B=np.zeros([(n-1)**2,(n-1)**2])
for i in range(n-1):
    for j in range(n-1):
        if j==0: 
            B[i*(n-1)+j,i*(n-1)+j+1]=h0/(32*h1**2)
            if i<n-2:
                B[i*(n-1)+j,(i+1)*(n-1)+j]=h0/(32*h1**2)
            if i>0:
                B[i*(n-1)+j,(i-1)*(n-1)+j]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j]=1-3*h0/(32*h1**2)

        elif j==n-2: 
            B[i*(n-1)+j,i*(n-1)+j-1]=h0/(32*h1**2)
            if i<n-2:
                B[i*(n-1)+j,(i+1)*(n-1)+j]=h0/(32*h1**2)
            if i>0:
                B[i*(n-1)+j,(i-1)*(n-1)+j]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j]=1-3*h0/(32*h1**2)
        
        elif i==0 :
            B[i*(n-1)+j,i*(n-1)+j+1]=h0/(32*h1**2)
            B[i*(n-1)+j,(i+1)*(n-1)+j]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j]=1-h0/(8*h1**2)
            B[i*(n-1)+j,i*(n-1)+j-1]=h0/(32*h1**2)

        elif i==n-2:
            B[i*(n-1)+j,i*(n-1)+j+1]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j-1]=h0/(32*h1**2)
            B[i*(n-1)+j,(i-1)*(n-1)+j]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j]=1-h0/(8*h1**2)

        else:
            B[i*(n-1)+j,i*(n-1)+j+1]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j-1]=h0/(32*h1**2)
            B[i*(n-1)+j,(i+1)*(n-1)+j]=h0/(32*h1**2)
            B[i*(n-1)+j,(i-1)*(n-1)+j]=h0/(32*h1**2)
            B[i*(n-1)+j,i*(n-1)+j]=1-h0/(8*h1**2)
x_d,y_d=np.meshgrid(xdate[1:-1],ydate[1:-1])
u=f(x_d,y_d)
u=u.T
u=u.flatten()
for t1 in tdate[1:-1]:
    tmp=np.matmul(B,u)
    u=np.linalg.solve(A,tmp)
u=u.reshape(n-1,n-1)
u=u.T
u_true=g(x_d,y_d,tmx)
er=abs(u-u_true).max()
err=np.linalg.norm(u-u_true,ord=2)/(n-1)**2
print(er)

print(u-u_true)
