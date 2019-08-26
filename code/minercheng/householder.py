'''
基于householder变换的QR分解
作者：陈春雨
时间：2019-8-25
'''
import numpy as np
import copy
#householder变换
def house(x):
    xg=0
    for x1 in x[1:]:
        xg+=x1**2
    if xg==0:
        if x[0]<0:
            x[0]*=2
            beta=2/(x[0]**2)
        else:
            x[0]=0
            beta=0
    else:
        al=np.sqrt(x[0]**2+xg)
        if x[0]<0:
            x[0]=x[0]-al
        else:
            x[0]=-xg/(x[0]+al)
        beta=2/(x[0]**2+xg)
    return x,beta
#QR分解
def QR(a):
    a=a.astype(float)
    (m,n)=a.shape
    q=np.identity(m)
    for i in range(n):
        y=copy.deepcopy(a[i:,i])
        v,beta=house(y)
        v=np.array([v])
        tmp=np.matmul(v,a[i:,i:])
        a[i:,i:]-=beta*np.matmul(v.T,tmp)
        tmp=np.matmul(q[:,i:],v.T)
        q[:,i:]-=beta*np.matmul(tmp,v)
    return q,a
#测试
a=np.array([[1,2,5],[5,4,7],[6,54,8]])
mm,mmm=QR(a)
print(mmm)
print(np.matmul(mm,mmm))















