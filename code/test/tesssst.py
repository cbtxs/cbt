import numpy as np

def lim(x):
    y = x*np.log(x)/((1 + np.log(x))**2)
    return y
print(lim(10000000000))

