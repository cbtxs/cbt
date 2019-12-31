import numpy as np
import matplotlib.pyplot as plt
import copy
def f(x, y):
    z=(np.exp(x)+1)*y**2 + 2*y*np.exp(x**2) - 2*y*np.exp(2*x-1) + np.exp(-x**2-1)
    return z
n=1555
x_0=np.linspace(-2,2,n)
y_0=copy.deepcopy(x_0)
for i in range(n):
    y_0[i]=f(x_0[i], -5)
plt.plot(x_0,y_0)
plt.show()
