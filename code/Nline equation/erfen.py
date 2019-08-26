import numpy as np

def ff(x):
    y=x**6-x-1
    return y
a,b=1,2
c=a
error=0.00000001
while abs(b-a)>error and abs(ff(c))>error:
    h=(b-a)/2
    c=a+h
    if np.sign(ff(c))==np.sign(ff(a)):
        a=c
    else:
        b=c
print(c)
