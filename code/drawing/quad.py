import numpy as np
import matplotlib.pyplot as plt
x,y=0,0
#直角坐标系下的坐标

x_qd=np.array([1+x,-1-x,-1+x,1-x,1+x,-1+x])#四边形坐标
y_qd=np.array([1+y,1-y,-1+y,-1-y,1+y, -1+y])
x_pi=np.array([1,-1,-1,1,1])#平行四边形坐标
y_pi=np.array([1,1,-1,-1,1])
x_mid=np.array([0,-1,0,1,0])#中点坐标
y_mid=np.array([1,0,-1,0,1])
A=np.array([[1,np.sqrt(2)/4],[0,3*np.sqrt(2)/4]])#变换矩阵


#原四边形
#qurd=np.array([x_qd,y_qd])
#x_qd=np.matmul(A[0,:],qurd)
#y_qd=np.matmul(A[1,:],qurd)
s_qd = ['$0$','$1$', '$2$', '$3$', '$0$']

#平行四边形
pill=np.array([x_pi,y_pi])
x_pi=np.matmul(A[0,:],pill)
y_pi=np.matmul(A[1,:],pill)


#中点
mid=np.array([x_mid,y_mid])
x_mid=np.matmul(A[0,:],mid)
y_mid=np.matmul(A[1,:],mid)
s_mid = ['$m_0$','$m_1$', '$m_2$', '$m_3$', '$m_0$']


s_e = ['$e_0$','$e_1$', '$e_2$', '$e_3$', '$e_0$']

a=np.array([-1.5,3])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')







plt.plot(x_qd,y_qd,color='black')

plt.plot([0, 0], [1, 1], color = 'black')



plt.text(x_qd[0]+0.2,y_qd[0],s_qd[2], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(x_qd[1]-0.1,y_qd[1],s_qd[3], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(x_qd[2]-0.1,y_qd[2]-0.1,s_qd[0], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(x_qd[3]+0.25,y_qd[3]-0.13,s_qd[1], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)



plt.xlim(-2,2)
plt.ylim(-2,2)


plt.show()











