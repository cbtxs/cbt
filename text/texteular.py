import numpy as np
import matplotlib.pyplot as plt
N=10001
def eular(x,y):
    return 2*y**(0.5)          
xdate=np.linspace(0,1,N)
ydate=np.array([1])
ydate2=(xdate+1)**2
for i in range(N)[1:]:
   m=ydate[i-1]+eular(xdate[i-1],ydate[i-1])/(N-1)
   ydate=np.append(ydate,m)
   print(m)
plt.plot(xdate,ydate-ydate2)
plt.plot(xdate,ydate)
plt.plot(xdate,ydate2)
plt.show()
