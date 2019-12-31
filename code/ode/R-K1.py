"""               
隐式Runge-Kutta法求解常微分方程数值解   
                               
                               
Author: 陈春雨                 
Date: 2019-7-10    
"""




import numpy as np
import matplotlib.pyplot as plt
import copy

a, b = 0, 10           # 区间（a,b）
c = 10          # 初值解y(a)=c
h = 0.01       # 剖分N次
def f(x,y):
    k = 5000*y - 250*y**2
    return k
def j(x):
    z=np.exp(x)
    return z
xdate=np.arange(a,b+h,h)
ydate=np.array([c])
ydate2=j(xdate)
for x in xdate[:-1]:
    l,k=0,10
    #不动点原理解非线性方程
    while abs(l-k)>=1e-10:
        l=copy.deepcopy(k)
        k=f(x+h/2,ydate[-1]+h*l/2)
    m=ydate[-1]+k*h
    ydate=np.append(ydate,m)
print(ydate)
plt.ylabel('erro')
plt.xlabel('x')
plt.plot(xdate,ydate-ydate2)
plt.show()
