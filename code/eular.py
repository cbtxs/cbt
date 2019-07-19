import numpy as np
import matplotlib.pyplot as plt
a=0           # 区间（a,b）
b=1
c=1           # 初值解y(a)=c
N=10001       # 剖分N次
def eular(x,y):
    return -y
xdate=np.linspace(a,b,N)
ydate=np.array([c])
ydate2=np.exp(-xdate)
for i in range(N)[1:]:
    m=ydate[i-1]+(b-a)*eular(xdate[i-1],ydate[i-1])/(N-1)
    ydate=np.append(ydate,m)
plt.ylabel('erro')
plt.xlabel('x')
plt.plot(xdate,ydate-ydate2)
plt.show()
