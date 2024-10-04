import numpy as np
M = np.array([[1,2,2],[4,5,6],[7,8,9]])
b=[1,2,3]
D = np.linalg.det(M)
x = []
for i in range(len(b)):
    M1 = np.copy(M)
    M1[:,i] = b
    d = np.linalg.det(M1)/D
    x.append(d)
print(x)    