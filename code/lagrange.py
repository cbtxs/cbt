"""               
Lagrange插值                               
                               
Author: 陈春雨                 
Date: 2019-5-5                
""" 
import matplotlib.pyplot as plt
import numpy as np
n=10
def RUNGR(x):
    y=1/(1+x**2)
    #print(y)
    return y
xdate=np.linspace(-5,5,n+1)#选取节点
ydate=RUNGR(xdate)#节点函数值
#定义Lagrange函数
def LG(x):
    shuju=[0,1,2,3,4,5,6,7,8,9,10]
    y=0
    lOg=[0,1,2,3,4,5,6,7,8,9,10]
    for i in shuju:
        lg=[0,1,2,3,4,5,6,7,8,9,10]
        shuju.remove(i)
        M=1
        for j in shuju:
            lg[i]=M*(x-xdate[j])/(xdate[i]-xdate[j])
            M=lg[i]
        shuju=[0,1,2,3,4,5,6,7,8,9,10]#因为shuju改变了如果不改回来就不能让i从0到10
        lOg[i]=M*ydate[i]
        y+=lOg[i]
    return y
#画函数图像
x1= np.arange(-5.0, 5.0, 0.0001)
y1=LG(x1)
y2=RUNGR(x1)
plt.plot(x1, y1,'b')
plt.plot(x1, y2,'r')
#plt.plot(x1,y2-y1)
plt.show()

