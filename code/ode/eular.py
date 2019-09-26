"""               
eular法求解常微分方程数值解   
                               
                               
Author: 陈春雨                 
Date: 2019-7-10    
"""




import numpy as np
import matplotlib.pyplot as plt

a,b=1,2           # 区间（a,b）
c=2/5           # 初值解y(a)=c
h=0.1       # 剖分N次
def eular(x,y):
    z=x**3-y/x
    k=-y
    return z
def j(x):
    y=x**4/5+1/(5*x)
    z=np.exp(-x)
    return y
xdate=np.arange(a,b+h,h)
ydate=np.array([c])
ydate2=j(xdate)
for x in xdate[:-1]:
    m=ydate[-1]+eular(x,ydate[-1])*h
    ydate=np.append(ydate,m)
plt.ylabel('erro')
plt.xlabel('x')
plt.plot(xdate,ydate-ydate2)
plt.show()
