"""
对runge函数三次样条插值


Author: 陈春雨
Date: 2019-7-27
"""





import numpy as np
import matplotlib.pyplot as plt

n=10
def runge(x):
    y=1/(1+x**2)
    return y
xdate=np.linspace(-5,5,n+1)
ydate0=runge(xdate)
#*********************************************
#追赶法求线性方程组
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
#追赶法结束
#***********************
#计算节点的导数ydate1
l=2*np.identity(n+1)
u=np.arange(n+1).astype(float)
print(xdate)
u[-1]=3*((ydate0[n]-ydate0[n-1])/(xdate[n]-xdate[n-1]))
u[0]=3*((ydate0[1]-ydate0[0])/(xdate[1]-xdate[0]))
l[0,1]=1
l[-1,-2]=1
for i in range(n)[1:]:
    l[i,i+1]=(xdate[i]-xdate[i-1])/(xdate[i+1]-xdate[i-1])
    l[i,i-1]=1-l[i,i+1]
    u[i]=3*((1-l[i,i+1])*(ydate0[i]-ydate0[i-1])/(xdate[i]-xdate[i-1])+l[i,i+1]*(ydate0[i+1]-ydate0[i])/(xdate[i+1]-xdate[i]))
ydate1=catch(l,u)
def hermite(x):
    for i in range(10):
        if xdate[i]<=x<=xdate[i+1]:
            ai=(1+2*(x-xdate[i])/(xdate[i+1]-xdate[i]))*(((x-xdate[i+1])/(xdate[i]-xdate[i+1]))**2)
            aii=(1+2*(x-xdate[i+1])/(xdate[i]-xdate[i+1]))*(((x-xdate[i])/(xdate[i+1]-xdate[i]))**2)
            bi=(x-xdate[i])*(((x-xdate[i+1])/(xdate[i]-xdate[i+1]))**2)
            bii=(x-xdate[i+1])*(((x-xdate[i])/(xdate[i+1]-xdate[i]))**2)
            z=ydate0[i]*ai+ydate1[i]*bi+ydate0[i+1]*aii+ydate1[i+1]*bii
    return z
print(hermite(3.2)-runge(3.2))
x1=np.linspace(-5,5,10000)
y1=runge(x1)
y2=np.array([])
for i in x1:
    y2=np.append(y2,hermite(i))
plt.plot(x1,y1,'b')
plt.plot(x1,y2,'r')
plt.show()

