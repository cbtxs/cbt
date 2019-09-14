'''
Rayleigh商迭代求矩阵特征值特征向量

作者：陈春雨
date：2019-9-3
'''

import numpy as np
import copy

#LU分解
def gecplu(x):
    (n,n)=x.shape
    l=np.identity(n)
    p=np.arange(n)
    u=x.astype(float)
    for i in range(n-1):
        k=np.argmax(abs(u[i:,i]))
        k=k+i
        if i!=k:
            tmp=copy.deepcopy(u[i,:])
            u[i,:]=copy.deepcopy(u[k,:])
            u[k,:]=copy.deepcopy(tmp)
            tmmp=copy.deepcopy(p[i])
            p[i]=copy.deepcopy(p[k])
            p[k]=copy.deepcopy(tmmp)
        for j in range(n)[i+1:]:
            u[j,i]=u[j,i]/u[i,i]
            u[j,i+1:]=u[j,i+1:]-u[j,i]*u[i,i+1:]
    for i in range(n):
        for j in range(i):
            l[i,j]=u[i,j]
            u[i,j]=0
    return l,u,p


def gauss(A,b):           #要求b为一位数组np.array([])型的
    (n,n)=A.shape
    (l,u,p)=gecplu(A)
    tmp=copy.deepcopy(b)
    for i in range(n):
        b[i]=copy.deepcopy(tmp[p[i]])
    #计算ly=b
    y=b.astype(float)
    for i in range(n)[1:]:
        for j in range(n)[:i]:
            y[i]=y[i]-l[i,j]*y[j]
    x=b.astype(float)
    #计算ux=y
    for i in range(n):
        i=n-i-1
        for j in range(n)[i+1:]:
            y[i]=y[i]-u[i,j]*x[j]
        x[i]=y[i]/u[i,i]
    return x
error=0.01

#Rayleigh商迭代
def Rayleigh(a):
    a=a.astype(float)
    (n,n)=a.shape
    p=np.array([3/np.sqrt(10),0.01,0])
    k=0
    e=np.identity(n)
    l1,l2=0,1
    t=np.dot(p,np.matmul(a,p))
    while abs(l1-l2)>error:
        tmp=copy.deepcopy(a-t*e)
        pp=gauss(tmp,p)
        mo=np.dot(pp,pp)
        p=pp/np.sqrt(mo)
        tmp=np.matmul(a,p.T)
        t=np.dot(p,tmp)
        l2=copy.deepcopy(l1)
        l1=copy.deepcopy(t)
        k+=1
    return p,t
#测试

aa=np.array([[1,0,2],[0,2,0],[0,4,-1]])
l,n=Rayleigh(aa)
print(l,n)




















