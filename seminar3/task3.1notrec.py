n = int(input())
sp = [0] * n
sp[0] = 1
sp[1] = 1
for i in range(2,n):
    sp[i] = sp[i-1] + sp[i-2]
print(sp[n-1])