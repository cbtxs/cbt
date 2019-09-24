import numpy as np
import copy
def f(x,y):
    z=x**3-y/x
    return z
a,b=1,2
h=0.1
def g(x):
    y=x**4/5+1/(5*x)
    return y
xdate=np.arange(a,b+h,h)
y0=g(xdate)
ydate=np.array([2/5])


#三级三阶显式Runge-Kutta
ydate0=copy.deepcopy(ydate)
for x in xdate[:-1]:
    k1=f(x,ydate0[-1])
    k2=f(x+h/2,ydate0[-1]+k1*h/2)
    k3=f(x+h,ydate0[-1]-h*k1+2*h*k2)
    tmp=ydate0[-1]+h*(k1+k2*4+k3)/6
    ydate0=np.append(ydate0,tmp)
print(ydate0-y0)

























