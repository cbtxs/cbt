import numpy as np

class qhfem():
    def __int__(self, alp = 0.5, beta=0.5):
        self.alp = alp
        self.beta = beta

    def basic(self, xi, eta):
        val = np.zeros(4)
        val[0] = ((self.alp + self.beta +1)/((1 + self.alp)*(1 + self.beta)))*xi*eta-xi-eta+1
        val[1] = (-1/(1+self.beta))*xi*eta + xi
        val[2] = (1/((1+self.alp)*(1+self.beta)))*xi*eta
        val[3] = (-1/(1+self.beta))*xi*eta +eta
        return val
bas = qhfem()
print(bas.basic(0,0)) 
