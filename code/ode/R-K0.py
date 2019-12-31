import numpy as np
import copy
def f(x,y):
    z=x**3-y/x
    return z
a,b=0, 100
n=int(input('n='))
h=(b-a)/n
def g(x):
    y = 2
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
r0=ydate0-y0
error=abs(r0).max()
print('error=',error)

#三级四阶显式Heun
ydate1=copy.deepcopy(ydate)
for x in xdate[:-1]:
    k1=f(x,ydate1[-1])
    k2=f(x+h/3,ydate1[-1]+k1*h/3)
    k3=f(x+2*h/3,ydate1[-1]+2*h*k2/3)
    tmp=ydate1[-1]+h*(k1+k3*3)/4
    ydate1=np.append(ydate1,tmp)
r0=ydate1-y0    
error=np.linalg.norm(r0,ord=2)/n
print('error=',error)
#四级四阶显式kutta
ydate2=copy.deepcopy(ydate)
for x in xdate[:-1]:
    k1=f(x,ydate2[-1])
    k2=f(x+h/3,ydate2[-1]+k1*h/3)
    k3=f(x+2*h/3,ydate2[-1]-h*k1/3++h*k2)
    k4=f(x+h,ydate2[-1]+h*k1-h*k2+h*k3)
    tmp=ydate2[-1]+h*(k1+3*k2+k3*3+k4)/8
    ydate2=np.append(ydate2,tmp)
print(ydate2-y0)

#四级四阶显式Gill
ydate3=copy.deepcopy(ydate)
for x in xdate[:-1]:
    k1=f(x,ydate3[-1])
    k2=f(x+h/2,ydate3[-1]+k1*h/2)
    k3=f(x+h/2,ydate3[-1]+(np.sqrt(2)-1)*h*k1/2+(1-np.sqrt(2)/2)*h*k2)
    k4=f(x+h,ydate3[-1]-np.sqrt(2)*h*k2/2+h*(1+np.sqrt(2)/2)*k3)
    tmp=ydate3[-1]+h*(k1+(2-np.sqrt(2))*k2+(2+np.sqrt(2))*k3+k4)/6
    ydate3=np.append(ydate3,tmp)
print(ydate3-y0)





















