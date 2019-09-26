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

#两步的隐式Adams公式(解非线性方程)
ydate0=copy.deepcopy(ydate)
for x in xdate[:-1]:
    l,k=0,10
    while abs(l-k)>=1e-10:
        l=copy.deepcopy(k)
        k=ydate0[-1]+h*(f(x+h,l)+f(x,ydate0[-1]))/2
    ydate0=np.append(ydate0,k)
print(ydate0-y0)



#两部的隐式adms公式(化简)
ydate1=copy.deepcopy(ydate)
for x in xdate[:-1]:
    k=((1-h/(2*x))*ydate1[-1]+h*((x+h)**3+x**3)/2)/(1+h/(2*(x+h)))
    ydate1=np.append(ydate1,k)
print(ydate1-y0)

#改进的欧拉公式
ydate2=copy.deepcopy(ydate)
for x in xdate[:-1]:
    l0=ydate2[-1]+h*f(x,ydate2[-1])
    k0=ydate2[-1]+h*(f(x+h,l0)+f(x,ydate2[-1]))/2
    ydate2=np.append(ydate2,k0)
print(ydate2-y0)


#欧拉公式
ydate3=copy.deepcopy(ydate)
for x in xdate[:-1]:
    m=ydate3[-1]+f(x,ydate3[-1])*h
    ydate3=np.append(ydate3,m)
print(ydate3-y0)













