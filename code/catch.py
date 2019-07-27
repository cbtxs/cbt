import numpy as np

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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
