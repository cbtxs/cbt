import numpy as np
import copy
import time

def ff(x):
    y=2*x-6
    return y
a,b=0,1
error=0.00000001
def tx(x,h):
    (n,)=x.shape
    jifen=0
    for i in range(n-1):
        jifen+=x[i]+x[i+1]
    jifen*=h/2
    return jifen
t=np.array([[0,0]])
zero=np.array([[0,0]])
l=1
h=1
x0=np.array([a,b])
y0=np.array([ff(a),ff(b)])
while l>error:
    for i in range(h):
        t[i,0]=copy.deepcopy(t[i,1])
        if i==0:
            t[i,1]=tx(y0,(b-a)/h)
        else:
            t[i,1]=(4**i*t[i-1,1]-t[i-1,0])/(4**i-1)
    t=np.concatenate(t,zero,axis=0)
    zero0=np.zeros(h)
    h=h*2
    x0=np.linspace(a,b,h+1)
    y0=np.append(y0,zero0)
    for i in range(int(num1/2)):
        i=int(num1/2)-i
        y0[2*i]=copy.deepcopy(y0[i])
        y0[2*i-1]=ff(x0[2*i-1])
    l=abs(t[-1,1]-t[-2,1])
print(t[-2,1])
