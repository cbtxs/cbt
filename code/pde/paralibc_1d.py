import numpy as np
#############三对角矩阵线性方程组##############
def sdjlu(x):
    (n,n)=x.shape
    l=x.astype(float)
    u=np.identity(n)
    u[0,1]=l[0,1]/l[0,0]
    l[0,1]=0
    for i in range(n-1)[1:]:
        l[i,i]=l[i,i]-l[i,i-1]*u[i-1,i]
        u[i,i+1]=l[i,i+1]/l[i,i]
        l[i,i+1]=0
    l[-1,-1]=l[-1,-1]-l[-1,-2]*u[-2,-1]
    return l,u

def catch(A,b):       #计算Ax=b
    (n,n)=A.shape
    (l,u)=sdjlu(A)
    #计算ly=b
    y=b.astype(float)
    y[0]=y[0]/l[0,0]
    for i in range(n)[1:]:
        y[i]=(b[i]-l[i,i-1]*y[i-1])/l[i,i]
    #计算ux=y
    x=y.astype(float)
    for i in range(n-1):
        i=n-2-i
        x[i]=y[i]-u[i,i+1]*x[i+1]
    return x


##########向后差分格式#######
def f(x,t):
    y=np.sin(t)
    return y
def g(x):
    y=np.cos(np.pi*x)
    return y
def j(x,t):
    y=np.exp(-np.pi**2*t)*np.cos(np.pi*x)+1-np.cos(t)
    return y
#生成三对角矩阵
def sdj(a,b,n):
    x=a*np.identity(n)
    for i in range(n):
        if i!=0:
            x[i,i-1]=b
        if i!=n-1:
            x[i,i+1]=b
    return x
a,b=0,1
n=int(input('n='))
h0,h1=0.1/n,(b-a)/n
xdate=np.linspace(a,b,n+1)
tdate=np.arange(0,1+h0,h0)
#生成系数矩阵
A=np.eye(n-1)*(-2)+np.eye(n-1,k=1)+np.eye(n-1,k=-1)
A[0,0],A[-1,-1]=-1,-1
A=h0/(h1**2)*A-np.identity(n-1)
#初值
u=g(xdate[1:-1])
for t in tdate[1:]:
    b=-h0*f(xdate[1:-1],t)-u
    u=catch(A,b)
er=np.linalg.norm(u-j(xdate[1:-1],1),ord=1)/u.shape
#er=abs(u-j(xdate[1:-1],1)).max()
print(er)



















