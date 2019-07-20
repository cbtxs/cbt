import numpy as np
N=20
xdate=np.linspace(3,4,N+1)
ydate=np.linspace(3,4,N+1)
def f(x,y):
    z=x**2+y**2
    return z
def zxzb(x,y):
    for i in range(N):
        for j in range(N):
            if xdate[i]<=x<=xdate[i+1] and ydate[j]<=y<=ydate[j+1]:
                if(y-ydate[j])/(x-xdate[i])>=(ydate[j+1]-ydate[j])/(xdate[i+1]-xdate[i]):
                    a=(x-xdate[i])/(xdate[i+1]-xdate[i])
                    b=(ydate[j+1]-y)/(ydate[j+1]-ydate[j])
                    c=1-a-b
                    z=a*f(xdate[i+1],ydate[j+1])+b*f(xdate[i],ydate[j])+c*f(xdate[i],ydate[j+1])
                else:
                    a=(xdate[i+1]-x)/(xdate[i+1]-xdate[i])
                    b=(y-ydate[j])/(ydate[j+1]-ydate[j])
                    c=1-a-b
                    z=a*f(xdate[i],ydate[j])+b*f(xdate[i+1],ydate[j+1])+c*f(xdate[i+1],ydate[j])
    return z
print (f(3.6,3.2256)-zxzb(3.6,3.2256))
x1=np.linspace(3,4,100)
y1=np.linspace(3,4,100)
z1=np.array([])
for x11 in x1:
    for y11 in y1:
        z1=np.append(z1,f(x11,y11)-zxzb(x11,y11))
print(max(z1),min(z1))

