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
    z=np.sqrt(1-x**2-y**2)
    return z
def y1(x):
    return 0
def y2(x):
    return np.sqrt(1/4-(x-1/2)**2)
a,b=0,1
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
        z=np.append(z,kong)#用来存放被积函数值
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
    y=np.append(y,z)#用来存放含参量积分的函数值
    for i in range(int(num1/2)):
        i=int(num1/2)-i
        y[2*i]=copy.deepcopy(y[i])
        y[2*i-1]=fy(x[2*i-1])
    h2=(b-a)/(num1/2)
    s2=simposn(y,h2)
print(s2*2)#积分数值解
end=time.time()
print(end-star)
