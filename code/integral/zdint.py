import numpy as np

def ff(x):
    y=x**2
    return y
a,b=0,1
error=0.0001
def zd(h):
    x=np.arange(a,b,h)
    if x[-1]!=b:
       x=np.append(x,b)
    (n,)=x.shape
    y=0
    for i in range(n-1):
        y=y+ff((x[i]+x[i+1])/2)
    y*=h
    return y
h=0.4
l1,l2=0,1
while abs(l1-l2)/3>error:
    l1=zd(h)
    l2=zd(h/2)
    h=h/2
    print('***')
    print(l1-l2)
    print('***')
print('积分值=%f,步长=%f'%(l2,h))
