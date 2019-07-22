import numpy as np
import matplotlib.pyplot as plt

def runge(x):
    y=1/(1+x**2)
    return y
def runge1(x):
    y=-2*x/((1+x**2)**2)
    return y
xdate=np.linspace(-5,5,11)
ydate0=runge(xdate)
ydate1=runge1(xdate)
def hermite(x):
    for i in range(10):
        if xdate[i]<=x<=xdate[i+1]:
            ai=(1+2*(x-xdate[i])/(xdate[i+1]-xdate[i]))*(((x-xdate[i+1])/(xdate[i]-xdate[i+1]))**2)
            aii=(1+2*(x-xdate[i+1])/(xdate[i]-xdate[i+1]))*(((x-xdate[i])/(xdate[i+1]-xdate[i]))**2)
            bi=(x-xdate[i])*(((x-xdate[i+1])/(xdate[i]-xdate[i+1]))**2)
            bii=(x-xdate[i+1])*(((x-xdate[i])/(xdate[i+1]-xdate[i]))**2)
            z=ydate0[i]*ai+ydate1[i]*bi+ydate0[i+1]*aii+ydate1[i+1]*bii
    return z
print(hermite(3.2)-runge(3.2))
x1=np.linspace(-5,5,10000)
y1=runge(x1)
y2=np.array([])
for i in x1:
    y2=np.append(y2,hermite(i))
plt.plot(x1,y1,'b')
plt.plot(x1,y2,'r')
plt.show()
