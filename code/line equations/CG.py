import numpy as np
import copy 
import time
def CG(A,b):
    (n,n)=A.shape
    x0=np.zeros(n)+1
    r0=b-np.matmul(A,x0)
    bate=np.linalg.norm(r0,ord=2)
    for i in range(n+1):
        ro=np.einsum('i,i->',r0,r0)
        if i>1:
            mu=ro/ro0
            pm=r0+mu*pm
        else:
            pm=copy.deepcopy(r0)
        qm=np.matmul(A,pm)
        yl=ro/np.einsum('i,i->',pm,qm)
        x0=x0+yl*pm
        r1=copy.deepcopy(r0)
        r0=r0-yl*qm
        rels=np.linalg.norm(r0,ord=2)/bate
        if rels<1e-10:
            break
        ro0=copy.deepcopy(ro)
    if rels<1e-10:
        return x0
    else:
        return x0





from fealpy.mesh import IntervalMesh
from scipy.sparse.linalg import spsolve
from fealpy.functionspace import LagrangeFiniteElementSpace
def u(x):
    return np.cos(x)
p=int(input('p='))
n=int(input('n='))
node=np.array([0,1],dtype=np.float)
cell=np.array([[0,1]],dtype=np.int)
mesh=IntervalMesh(node,cell)
mesh.uniform_refine(n)
space=LagrangeFiniteElementSpace(mesh,p=p)
M=space.mass_matrix().toarray()
F=space.source_vector(u)
start1=time.time()
print(CG(M,F))
start2=time.time()
print(spsolve(M,F))
start3=time.time()
print('CG用时',start2-start1)
print('spsolve用时',start3-start2)

print(spsolve(M,F)-CG(M,F))






















