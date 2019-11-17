import numpy as np
import matplotlib.pyplot as plt
from fealpy.mesh import IntervalMesh
from fealpy.functionspace import LagrangeFiniteElementSpace


def u(p):
    pi = np.pi
    return np.exp(p**2)*np.cos(p+1)

def du(p):
    pi = np.pi
    return np.exp(p**2)*(np.cos(p+1)*2*p-np.sin(p+1))

p = int(input('p='))

def f(n):
# 准备网格
    node = np.array([0, 1], dtype=np.float)
    cell = np.array([[0, 1]], dtype=np.int)
    mesh = IntervalMesh(node, cell)
    mesh.uniform_refine(n=n)
    node = mesh.entity('node')
    cell = mesh.entity('cell')
#print(node)
#print(cell)
# 准备空间
    space = LagrangeFiniteElementSpace(mesh, p=p)
#ipoints = space.interpolation_points()
#uI = u(ipoints)

    uI = space.interpolation(u)

    error1 = space.integralalg.L2_error(u, uI)
    error2 = space.integralalg.L2_error(du, uI.grad_value)
    
    return error1, error2
for i in range(6)[2:]:
    er1, er2=f(i)
    print('加密%i次'%i)
    print('函数的误差:', er1)
    print('梯度的误差:', er2)
if 0:
    for i in range(5)[2:]:
        er1, er2=f(i)
        err1, err2=f(i+1)
        print('函数的误差阶数:\n',np.log2(err1/er1))
        print('梯度的误差阶数:\n',np.log2(err2/er2))
        print('***********************************')

if 0:
    def f(bc):
        ps = mesh.bc_to_point(bc) # ps: (NQ, NC)
        return (du(ps) - uI.grad_value(bc))**2

    qf = mesh.integrator(p+2)
    bc, ws = qf.get_quadrature_points_and_weights()
    # bc: (NQ, 2), ws: (NQ, )
    L = mesh.entity_measure('cell')
    error = np.sqrt(np.einsum('i, ij, j->', ws, f(bc), L))
    print(error)




if 0:
    def f(bc):
        ps = mesh.bc_to_point(bc) # ps: (NQ, NC)
        return (u(ps) - uI(bc))**2

    qf = mesh.integrator(p+2)
    bc, ws = qf.get_quadrature_points_and_weights()
# bc: (NQ, 2), ws: (NQ, )
    L = mesh.entity_measure('cell')
    error = np.sqrt(np.einsum('i, ij, j->', ws, f(bc), L))
    print(error)


if 0:
#print("积分点：\n", qf.quadpts)
#print("积分权重：\n", qf.weights)
    node = mesh.entity('node')
    cell = mesh.entity('cell')
    print("新节点：\n", node)
    phi = space.basis(bc)
# phi : (NQ, ldof)
    print("phi\n", phi)

    val = uI(bc)
# val: (NQ, NC)
#print("val:\n", val)


    gphi = space.grad_basis(bc)
# gphi: (NQ, NC, ldof)

    gval = uI.grad_value(bc)
# gval: (NQ, NC)

    fig, axes = plt.subplots(1, 2)
    mesh.add_plot(axes[0])
    #mesh.find_node(axes[0], node=ipoints, color='k')
    mesh.find_node(axes[0], node=node, color='r')

    idx = np.argsort(ipoints)
    axes[1].plot(ipoints[idx], uI[idx])
    plt.show()
