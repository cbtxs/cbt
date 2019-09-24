"""
simpson法计算函数二重积分


Author:陈春雨
date:2019-7-29
"""

import numpy as np
import matplotlib.pyplot as plt
import copy
import time
#计算ff(x,y)在[a,b]x[y1(x),y2(x)]的积分
star=time.time()
#定义积分
def ff(x,y):#定义ff(x,y)
    z=y*np.sqrt(1-y**2*np.sin(x)**2)
    return z
def y1(x):
    return 0
def y2(x):
    return 1
a,b=np.pi/4,3*np.pi/4
error0=0.000000001#含参量积分的误差
error1=0.00000001#二重积分的误差
def simposn(x,h):#积分数值解
    (n,)=x.shape
    int1=0
    for i in range(int((n-1)/2)):
        int1+=x[2*i]+4*x[2*i+1]+x[2*i+2]
    int1*=h/6
    return int1
def fy(x):#进行迭代，当含参量积分小于误差时输出含参量积分
    num0=1
    l1,l2=0,1
    y=np.array([y1(x),y2(x)])
    z=np.array([ff(x,y1(x)),ff(x,y2(x))])
    while abs(l1-l2)/15>error0:
        l1=l2
        kong=np.zeros(num0)
        num0=num0*2
        y=np.linspace(y1(x),y2(x),num0+1)
        z=np.append(z,kong)#用来存放被积函数值（用计算一重积分的方法计算会很慢）
        for i in range(int(num0/2)):
            i=int(num0/2)-i
            z[2*i]=copy.deepcopy(z[i])
            z[2*i-1]=ff(x,y[2*i-1])
        h1=abs(y2(x)-y1(x))/(num0/2)
        l2=simposn(z,h1)
    return l2

#含参量积分定义完成，之后只需将其看成一个函数即可
num1=1
x=np.array([a,b])
y=np.array([fy(a),fy(b)])
s1,s2=0,1
while abs(s1-s2)/15>error1:
    s1=copy.deepcopy(s2)
    z=np.zeros(num1)
    num1=num1*2
    x=np.linspace(a,b,num1+1)
    y=np.append(y,z)#用来存放含参量积分的函数值（用计算一重积分的方法计算会很慢）
    for i in range(int(num1/2)):
        i=int(num1/2)-i
        y[2*i]=copy.deepcopy(y[i])
        y[2*i-1]=fy(x[2*i-1])
    h2=(b-a)/(num1/2)
    s2=simposn(y,h2)
end=time.time()
































import numpy as np

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
h0,h1,h2=0.01,0.05,0.05
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
def js(t0):
    t=np.arange(e,t0+h0,h0)
    u=f(x_0,y_0)
    u=u.T
    u=u.flatten()
    A1=(h0/(4*(h1**2)))*A+np.identity(l)
    for t1 in t[1:]:
        b=np.zeros([m-2,n-2])
        #b[:,0]=g(xdate[1:-1],0,t1-h0)
        #b[:,-1]=g(xdate[1:-1],-1,t1-h0)
        b=b.flatten()
        u=np.matmul(A1,u)+(h0/(4*(h1**2)))*b
    u=u.reshape(m-2,n-2)
    return u.T
uu=js(0.02)/g(x_0,y_0,0.02)
print(uu)
print(g(x_0,y_0,0.1))



