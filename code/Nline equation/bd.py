import numpy as np

def ff(x):
    y=(x**2+21)/10
    return y
x0=2
error=0.0000000000001
while ff(x0)-x0>error:
    x0=ff(x0)
print(x0)
