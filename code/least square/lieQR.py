'''
列主元QR分解
作者：陈春雨
时间：2019-8-26
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
#列主元QR分解
def QR(a):
    a=a.astype(float)
    (m,n)=a.shape
    q=np.identity(m)
    p=np.identity(n)
    error=0.0000001
    for i in range(n):
        k=i
        su=0
        while su<error and k!=n:
            su=np.matmul(a[i:,k],a[i:,k])
            k=k+1
        if su>error:
            print(k)
            tmp=copy.deepcopy(a[:,k-1])
            a[:,k-1]=copy.deepcopy(a[:,i])
            a[:,i]=copy.deepcopy(tmp)
            tmp1=copy.deepcopy(p[:,k-1])
            p[:,k-1]=copy.deepcopy(p[:,i])
            p[:,i]=copy.deepcopy(tmp1)
            y=copy.deepcopy(a[i:,i])
            v,beta=house(y)
            v=np.array([v])
            tmp=np.matmul(v,a[i:,i:])
            a[i:,i:]-=beta*np.matmul(v.T,tmp)
            tmp=np.matmul(q[:,i:],v.T)
            q[:,i:]-=beta*np.matmul(tmp,v)
    return p,q,a
#测试
a=np.array([[1,2,1,4],[1,3,2,5],[1,4,3,8],[1,5,4,63],[1,6,5,9]])
mm,mmm,mmmm=QR(a)
print(np.matmul(a,mm))
print(np.matmul(mmm,mmmm))
print(mmmm)
