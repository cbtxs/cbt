'''
levinson算法求解Toepliz线性方程组

Author:陈春雨
date:2019-7-28
'''


def levinson(t,b):
    n=b.shape
    x=np.array([-b[0]])
    tmp1=0
    tnp1=0
    for i in range(n)[1:]:
        for j in range(i):
            tmp1=tmp1+t[j]*x[-j-1]
            tnp1=tnp+t[j]*y[j]
        if i==0:
                tmp2=tmp1+1
        if i>0:
            tmp2=tmp2*(1-tmp**2)
        tmp=(-t[i]-tmp1)/tmp2
        x=x-tmp*x[::-1]
        tnp=(b[i]-tmp1)/tnp1
        y=x+tnp*y[::-1]
        x=np.append(x,tmp)
        y=np.append(y,tnp)
    return y










