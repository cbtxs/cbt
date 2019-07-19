import matplotlib.pyplot as plt
import numpy as np
#import copy
n=10
def RUNGR(x):
    y=1/(1+x**2)
    return y
xdate=np.linspace(-5,5,n+1)#选取节点
ydate=RUNGR(xdate)
def FD(x):
    #shuju=[0,1,2,3,4,5,6,7,8,9,10]
    lo=[0,1,2,3,4,5,6,7,8,9,10]
    y=0
    for i in range(n):
        if i==0:
            if xdate[i]<x<xdate[i+1]:
                lo[i]=(x-xdate[i+1])/(xdate[i]-xdate[i+1])
            else:
                lo[i]=0
        elif i==n:
            if xdate[i-1]<=x<=xdate[i]:
                lo[i]=(x-xdate[i-1])/(xdate[i]-xdate[i-1])
            else:
                lo[i]=0
        elif xdate[i]<=x<=xdate[i+1]:
            lo[i]=(x-xdate[i+1])/(xdate[i]-xdate[i+1])
        elif xdate[i-1]<=x<=xdate[i]:
            lo[i]=(x-xdate[i-1])/(xdate[i]-xdate[i-1])
        else:
            lo[i]=0
    for j in range(n):
        y+=lo[j]*ydate[j]
    return y
print(FD(-4.0))
print(FD(0.2))
x1=np.arange(-5.0, 5.0, 0.01)
y1=[]
for v in x1:
    y1.append(FD(v))
y2=RUNGR(x1)
plt.plot(x1, y1,'g')
plt.plot(x1, y2,'r')    
