import numpy as np
def MNK(sp_x,sp_y):
    n = len(sp_x)
    sum_x = np.sum(sp_x)
    sum_y = np.sum(sp_y)
    x_squared = sp_x
    for elem in x_squared:
        elem = elem * elem
    sum_x_squared = np.sum(x_squared)
    xy = [0]*n
    for i in range(n):
        xy[i] = sp_x[i]*sp_y[i]
    sum_xy = np.sum(xy)
    a = (n*sum_xy - sum_x*sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return a , b
sp_x1 = np.array([0,1,2,3,4,5])
sp_y1 = np.array([0,1,2,3,4,5])
a1, b1 = MNK(sp_x1,sp_y1)
print(a1)
print(b1) 
 
