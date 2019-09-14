import numpy as np
import copy
import scipy.linalg
def f(x,y):
    z=np.cos(3*x)*np.sin(np.pi*y)
    return -z
def zj(x,y):
    z=np.cos(3*x)*np.sin(np.pi*y)/(9+np.pi**2)
    return z
def yyy(n):
    a,b=0,np.pi
    c,d=0,1
    h1=(b-a)/n
    h2=(d-c)/n
    xdate=np.linspace(a,b,n+1)
    ydate=np.linspace(c,d,n+1)
    uy_0=f(xdate[0],ydate)
    uy_1=f(xdate[-1],ydate)
    ux_0=np.zeros([n+1])
    ux_1=np.zeros([n+1])
    nn=(n-1)**2
    u=np.zeros([nn,nn])
    for i in range(nn):
        if (i+1)%(n-1)>=2 or (i+1)%(n-1)==0:
            u[i,i-1]=1/h2**2
        if (i+1)%(n-1)+1<=n-1 and (i+1)%(n-1)!=0:
            u[i,i+1]=1/h2**2
        if i-n+1>=0:
            u[i,i-n+1]=1/10**2
        if i+n-1<=nn-1:
            u[i,i+n-1]=1/10**2
        u[i,i]=-2*(1/h1**2+1/h2**2)
    b=np.zeros([n-1,n-1])
    for i in range(n-1):
        for j in range(n-1):
            b[i,j]=f(xdate[i+1],ydate[j+1])
    b[0,:]-=uy_0[1:-1]/h1**2
    b[-1,:]-=uy_1[1:-1]/h1**2
    b[:,0]-=ux_0[1:-1]/h2**2
    b[:,-1]-=ux_1[1:-1]/h2**2
    b=b.flatten()
    x=np.linalg.solve(u,b)
    b=b.reshape(n-1,n-1)
    x=x.reshape(n-1,n-1)
    kkk=np.zeros([n-1,n-1])
    for i in range(n-1):
        for j in range(n-1):
            kkk[i,j]=zj(xdate[i+1],ydate[j+1])
    error=np.max(abs(x-kkk))
    mmm=b/kkk
    nnn=np.diag(mmm[:,0])
    ppp=kkk/x
    qqq=np.diag(ppp[:,0])
    lll=np.matmul(nnn,qqq)
    bbb=b.flatten()
    lll=np.kron(lll,np.identity(n-1))
    zzz=np.linalg.solve(lll,bbb)
    x=x.flatten()
    print(np.matmul(lll-u,x))
    print(mmm,'******')
    return u,b,mmm
err=np.zeros(8)
err0=np.zeros(8)
for i in range(8)[3:]:
    l,m,n=yyy(i)














