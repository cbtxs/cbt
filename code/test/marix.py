import numpy as np

aa=np.array([[4, 2, 3, 0], [2, 2, 2, 2], [0, -7, 0, 0]
    ,[1, 2, -1, 5]])
bb1=aa[:-1,1:]
bb2=aa[:-1][:,[0,2,3]]
bb3=aa[:-1][:,[0,1,3]]
bb4=aa[:-1][:,[0,1,2]]
print(np.linalg.det(bb1))
print(np.linalg.det(bb2))
print(np.linalg.det(bb3))
print(np.linalg.det(bb4))
print(aa)
