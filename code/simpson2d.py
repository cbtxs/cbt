"""
simpson法计算函数二重积分


Author:陈春雨
date:2019-7-29
"""

import numpy as np
import matplotlib.pyplot as plt
import copy

#计算ff(x,y)在[a,b]x[y1(x),y2(x)]的积分

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
error1=0.000001#二重积分的误差

#开始计算
def zd(x,h):#含参量积分数值解
    y=np.linspace(y1(x),y2(x),h+1)
    int0=0
    if y!=[]:
        (n,)=y.shape
        for i in range(n-1):
            int0+=ff(x,y[i])+4*ff(x,(y[i]+y[i+1])/2)+ff(x,y[i+1])
        int0=int0*abs(y2(x)-y1(x))/(6*h)
    return int0
def fy(x):#进行迭代，当含参量积分小于误差时输出含参量积分
    h=1
    l1,l2=0,1
    while abs(l1-l2)/15>error0:
        l1=zd(x,h)
        l2=zd(x,h*2)
        h*=2
    return l2
#含参量积分定义完成，之后只需将其看成一个函数即可
def f(x):#积分数值解
    (n,)=x.shape
    int1=0
    for i in range(int((n-1)/2)):
        int1+=x[2*i]+4*x[2*i+1]+x[2*i+2]
    int1*=(b-a)/(6*((n-1)/2))
    return int1
h=1
x=np.array([a,b])
y=np.array([fy(a),fy(b)])
s1,s2=0,1
while abs(s1-s2)/15>error1:
    s1=copy.deepcopy(s2)
    z=np.zeros(h)
    h=h*2
    x=np.linspace(a,b,h+1)
    y=np.append(y,z)#用来存放含参量积分的函数值（用计算一重积分的方法计算会很慢）
    for i in range(int(h/2)):
        i=int(h/2)-i
        y[2*i]=copy.deepcopy(y[i])
        y[2*i-1]=fy(x[2*i-1])
    s2=f(y)
print(s2)#积分数值解
