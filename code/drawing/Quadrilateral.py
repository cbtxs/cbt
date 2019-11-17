import numpy as np
import matplotlib.pyplot as plt
x,y=1/3,1/4
#直角坐标系下的坐标

x_qd=np.array([1+x,-1-x,-1+x,1-x,1+x])#四边形坐标
y_qd=np.array([1+y,1-y,-1+y,-1-y,1+y])
x_pi=np.array([1,-1,-1,1,1])#平行四边形坐标
y_pi=np.array([1,1,-1,-1,1])
x_mid=np.array([0,-1,0,1,0])#中点坐标
y_mid=np.array([1,0,-1,0,1])
A=np.array([[1,np.sqrt(2)/4],[0,3*np.sqrt(2)/4]])#变换矩阵
qurd=np.array([x_qd,y_qd])
x_qd=np.matmul(A[0,:],qurd)
y_qd=np.matmul(A[1,:],qurd)
pill=np.array([x_pi,y_pi])
x_pi=np.matmul(A[0,:],pill)
y_pi=np.matmul(A[1,:],pill)
mid=np.array([x_mid,y_mid])
x_mid=np.matmul(A[0,:],mid)
y_mid=np.matmul(A[1,:],mid)
axis close
plt.plot(x_qd,y_qd,color='black')
plt.plot(x_pi,y_pi,color='black',linestyle='--')
plt.plot(x_mid,y_mid,color='black',linestyle='--')
plt.plot([x_mid[1],0],[y_mid[1],0],color='black',linestyle='--')
plt.plot([x_mid[2],0],[y_mid[2],0],color='black',linestyle='--')
plt.annotate("", xy=(x_mid[3],y_mid[3]), xytext=(0, 0),
        arrowprops=dict(facecolor='black'))
plt.annotate("", xy=(x_mid[0],y_mid[0]), xytext=(0, 0),
        arrowprops=dict(facecolor='black'))
plt.show()
















