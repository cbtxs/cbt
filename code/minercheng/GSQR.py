'''
G-S法QR分解

作者：陈春雨
时间：2019-8-25
'''

import numpy as np

def GS(x):
    (m,n)=x.shape
    q=np.zeros([m,n])
    r=np.zeros([n,n])
    for i in range(n):
        q[:,i]=x[:,i]
        for j in range(n)[:i]:
            r[j,i]=np.dot(x[:,i],q[:,j])
            q[:,i]-=r[j,i]*q[:,j]
        r[i,i]=np.sqrt(np.dot(q[:,i],q[:,i]))
        q[:,i]/=r[i,i]
    return q,r
a=np.array([[1,2,3],[4,1,5]])
mm,mmm=GS(a)
print(np.matmul(mm,mmm))
