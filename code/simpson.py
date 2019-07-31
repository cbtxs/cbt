"""
simpson法计算函数数值积分


Author:陈春雨
date:2019-7-29
"""

import numpy as np
#计算ff(x)在[a,b]上的积分
def ff(x):
    y=(np.cos(x)**3-1)/(-3*np.sin(x)**2)
    return y
a,b=np.pi/4,3*np.pi/4#积分区间
error=0.0001#误差
def zd(h):
    x=np.linspace(a,b,h+1)
    (n,)=x.shape
    y=0
    for i in range(n-1):
        y+=ff(x[i])+4*ff((x[i]+x[i+1])/2)+ff(x[i+1])
    y*=(b-a)/(6*h)
    return y
h=1
l1,l2=0,1
while abs(l1-l2)/16>error:
    l1=zd(h)
    l2=zd(h*2)
    h=h*2
print('积分值=%f,步长=%f'%(l2,h))
