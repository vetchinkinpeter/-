import numpy as np
n = 5
N = np.zeros((n,n))
count = 1
dx = 1
dy = 0
x = 0
y = 0
for i in range(n*n):
    N[y][x] = count 
    count = count +  1
    if (x + dx < n) and (y + dy < n) and (x + dx >-1) and (y+dy > -1) and N[y+dy][x+dx] == 0:
        
        x = x + dx 
        y = y + dy
    else:
        dx, dy = -dy, dx
        x = x + dx 
        y = y + dy

print(N)        


