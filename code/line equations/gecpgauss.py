"""
选主元高斯消去法（A,b）放一起进行行变换

Author: 陈春雨
Date: 2019-7-27
"""


import numpy as np
import copy

#LU分解
def lu(x):
    (n,nn)=x.shape
    l=np.identity(n)
    u=x.astype(float)
    for i in range(n-1):
        k=np.argmax(abs(u[i:,i]))
        k=k+i
        if i!=k:
            tmp=copy.deepcopy(u[i,:])
            u[i,:]=copy.deepcopy(u[k,:])
            u[k,:]=copy.deepcopy(tmp)
        for j in range(n)[i+1:]:
            l[j,i]=u[j,i]/u[i,i]
            u[j,:]=u[j,:]-l[j,i]*u[i,:]
    return u
def gecpgauss(A,b):
    B=np.concatenate((A.T,b),axis=0)
    tm=lu(B.T)
    b=tm[:,-1]
    u=tm[:,0:-1]
    (n,n)=u.shape
    x=copy.deepcopy(b.astype(float))
    for i in range(n):
        i=n-1-i
        for j in range(n)[i+1:]:
            b[i]=b[i]-u[i,j]*x[j]
        x[i]=b[i]/u[i,i]
    return x
aa=np.array([[3.8,4.6,5.443,6.882],
    [8.674,9.423,10.255,6582.5666],
    [6.44,8.87,28.4,3.39],
    [20.65,43456.499,45.62,69.02]])
bb=np.sum(aa,axis=1)
bb=np.array([bb])
print(gecpgauss(aa,bb))



def inv(a):
    a=a.astype(float)
    (n,n)=a.shape
    print(n)
    b=np.identity(n)
    aa=copy.deepcopy(a)
    for i in range(n):
        cc=np.array([b[:,i]])
        aa[:,i]=gecpgauss(a,cc)
    return aa
aaa=np.array([[1,8,-1],[0,3,0],[0,4,1]])
aaaa=inv(aaa)
bbb=np.array([[1,0,2],[0,2,0],[0,4,-1]])
print(np.matmul(aaa,np.matmul(bbb,aaaa)))
