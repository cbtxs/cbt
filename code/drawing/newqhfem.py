import numpy as np
import matplotlib.pyplot as plt


alp, beta = 0.5, 0.5
val=np.array([[0, 0], [1, 0], [1+alp, 1+beta], [0 ,1], [0, 0]])
A = np.array([[1, 0.2], [0, 1]])
val = np.einsum('ij,kj->ki', A, val)
print(val)
plt.plot(val[:,0], val[:, 1], color='black')

s_qd = ['$A_0$','$A_1$', '$A_2$', '$A_3$', '$A_0$']

plt.annotate("", xy=(val[1, 0],val[1, 1]), xytext=(0, 0),
        arrowprops=dict(facecolor='black'))
plt.annotate("", xy=(val[3, 0],val[3, 1]), xytext=(0, 0),
        arrowprops=dict(facecolor='black'))


plt.text(val[0, 0],val[0, 1]-0.1,s_qd[0], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(val[1, 0]+0.1,val[1, 1]-0.1,s_qd[1], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(val[2, 0]+0.1,val[2, 1]+0.01,s_qd[2], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(val[3, 0],val[3, 1]+0.05,s_qd[3], family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)

plt.text(0.5,0.1,'$r$', family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)
plt.text(0.05,0.5,'$s$',  family='serif', 
            style='italic', ha='right', wrap=True, fontsize=25)


plt.xlim(-0.2,2)
plt.ylim(-0.2,2)



plt.show()
