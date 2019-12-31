import numpy as np



alp = 0.5
beta =0.2
def basic(xi, eta):
    val = np.zeros(4)
    val[0] = (( alp +  beta +1)/((1 +  alp)*(1 +  beta)))*xi*eta-xi-eta+1
    val[1] = (-1/(1+ beta))*xi*eta + xi
    val[2] = (1/((1+ alp)*(1+ beta)))*xi*eta
    val[3] = (-1/(1+ alp))*xi*eta +eta
    return val
val=np.array([[0, 0], [1, 0], [1+alp, 1+beta], [0 ,1]])
for i in range(4):
    print(basic(val[i, 0], val[i,1]))
mm=np.sum(val, axis=0)
print(val)
print(basic(mm[0]/4,mm[1]/4))


A = np.array([[1/2+alp/4, alp/4],[beta/4, 1/2+beta/4]])
F = np.array([(2+3*alp)/4, (2+3*beta)/4])
b = np.linalg.solve(A, F)
print(b-1)
al, be= b[0], b[1]

p=4*(al**2+be**2-1)

d0=(1-al)*(be-1)*(al+be+1)/p
print(d0)















