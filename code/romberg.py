import numpy as np
import copy
import time

def ff(x):
    y=4/(1+x**2)
    return y
a,b=0,1
error=0.000000000001
def tx(x,h):
    (n,)=x.shape
    jifen=0
    for i in range(n-1):
        jifen=jifen+x[i]+x[i+1]
    jifen=jifen*h/2
    return jifen
t=np.array([[0,0]]).astype(float)
zero=np.array([[0,0]])
l=1
h=1
k=1
x0=np.array([a,b])
y0=np.array([ff(a),ff(b)])
while l>error:
    for i in range(k):
        t[i,0]=copy.deepcopy(t[i,1])
        if i==0:
            mm=(b-a)/h
            t[i,1]=tx(y0,mm)
        else:
            t[i,1]=(4**i*t[i-1,1]-t[i-1,0])/(4**i-1)
    t=np.concatenate([t,zero],axis=0)
    zero0=np.zeros(h)
    h=h*2
    x0=np.linspace(a,b,h+1)
    y0=np.append(y0,zero0)
    for i in range(int(h/2)):
        i=int(h/2)-i
        y0[2*i]=copy.deepcopy(y0[i])
        y0[2*i-1]=ff(x0[2*i-1])
    if k>1:
        l=abs(t[-2,1]-t[-3,0])
    k+=1
print(t[-2,1])
