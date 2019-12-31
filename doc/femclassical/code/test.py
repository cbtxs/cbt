import numpy as np
import matplotlib.pyplot as plt

x0=np.array([1, 2])
x1=np.array([4, 0])
x2=np.array([8, 4])
x3=np.array([2, 6])
def x_0(x):
    xi=x[0]
    eta=x[1]
    y=xi*(x1 - x0) + eta*((x3 - x0)+xi*((x2 - x3) - (x1 - x0))) + x0
    return y
A=np.array([x0, x1, x2, x3])
B=np.zeros([4,2])
B[1, :] = np.array([1, 0])
B[3, :] = np.array([0, 1])
B[2, :] = np.array([1, 1])
B=B.T
print(B)
for i in range(4):
    print(x_0(B[:,i]))
def x_xi(xi, eta):
    y=(x1 - x0) + ((x2 - x3) - (x1 - x0))*eta
    return y
def x_eta(xi, eta):
    y=(x3 - x0)+xi*((x2 - x3) - (x1 - x0))
    return y
def f(x):
    y=x[1]+x[0]**2
    return y
def ff(x):
    x=x_0(x)
    y=x[1]+x[0]**2
    return y
xi=np.array([1/2,1/2])
xy=x_0(xi)
A=np.array([x_xi(xi[0],xi[1]),x_eta(xi[0],xi[1])])
print(xy+0.0001*(np.array([1,0])))
a11=(ff(xi+0.0001*(np.array([1,0])))-ff(xi))/0.0001
a12=(ff(xi+0.0001*(np.array([0,1])))-ff(xi))/0.0001
a21=(f(xy+0.0001*(np.array([1,0])))-f(xy))/0.0001
a22=(f(xy+0.0001*(np.array([0,1])))-f(xy))/0.0001
aa=np.array([a11,a12])
bb=np.array([a21,a22])
print(aa)
print(bb)
print(np.einsum('i,ij->j',bb,A.T))

