'''
基于Givens变换的QR分解
作者：陈春雨
时间：2019-8-26
'''
import numpy as np
import copy

def givens(x,y):
    if y==0:
        if x>=0:
            c,s=1,0
        else:
            c,s=-1,0
    else:
        if abs(y)>abs(x):
            tmp=x/y
            s=np.sign(y)/(np.sqrt(1+tmp**2))
            c=s*tmp
        else:
            tmp=y/x
            c=np.sign(x)/(np.sqrt(1+tmp**2))
            s=c*tmp
    z=np.array([[c,s],[-s,c]])
    return z
def QR(a):
    a=a.astype(float)
    (m,n)=a.shape
    q=np.identity(m)
    for i in range(n):
        for j in range(m)[i+1:]:
            G=givens(a[i,i],a[j,i])
            a[[i,j],i:]=np.matmul(G,a[[i,j],i:])
            q[:,[i,j]]=np.matmul(q[:,[i,j]],G.T)
    return q,a
a=np.array([[2,2,1,4],[1,3,2,5],[1,4,3,8],[1,5,55,63],[1,6,5,9]]) 
mmm,mmmm=QR(a) 
print(np.matmul(mmm,mmmm)) 
print(mmmm)








