"""
simpson法计算函数数值积分


Author:陈春雨
date:2019-7-29
"""

import numpy as np
import time
import copy
star=time.time()
#计算ff(x)在[a,b]上的积分
def ff(x):
    y=np.sin(x)**5
    return y
a,b=0, np.pi/2#积分区间
error=0.00000001#误差
def f(x):#积分数值解
    (n,)=x.shape
    int1=0
    for i in range(int((n-1)/2)):
        int1+=x[2*i]+4*x[2*i+1]+x[2*i+2]
    int1*=(b-a)/(6*((n-1)/2))
    return int1
h=1
x=np.array([a,b])
y=np.array([ff(a),ff(b)])
s1,s2=0,1
while abs(s1-s2)/15>error:
    s1=copy.deepcopy(s2)
    z=np.zeros(h)
    h=h*2
    x=np.linspace(a,b,h+1)
    y=np.append(y,z)#用来存放含参量积分的函数值（用计算一重积分的方法计算会很慢）
    for i in range(int(h/2)):
        i=int(h/2)-i
        y[2*i]=copy.deepcopy(y[i])
        y[2*i-1]=ff(x[2*i-1])
    print((b-a)/h)
    s2=f(y)
print('积分值=%f,步长=%f'%(s2,(b-a)/h))
end=time.time()
print(end-star)
print(8/15)
