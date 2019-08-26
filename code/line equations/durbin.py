'''
Yule-Walker 方程的Durbin算法

Author:陈春雨
date：2019-7-28
'''


import numpy as np

def durbin(b):
    n=b.shape
    x=np.array([-b[0]])
    tmp1=0
    for i in range(n)[1:]:
        for j in range(i):
            tmp1=tmp1+b[j]*x[-j-1]
        if i==0:
                tmp2=tmp1+1
        if i>0:
            tmp2=tmp2*(1-tmp**2)
        tmp=(-b[i]-tmp1)/tmp2
        z=x[::-1]
        x=x-tmp*z
        x=np.append(x,tmp)
    return x

