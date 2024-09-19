n = int(input())
sp = list(map( int , input().split()))
up = 0
down = 0
mid = 0
mediana = 0
for i in range(n):
    up = 0
    down = 0
    mid = 0
    for j in range(n):
        if sp[i] > sp[j]:
            up += 1
        if sp[i] < sp[j]:
            down += 1
        if sp[i] == sp[j]:
            mid += 1
    if (up + mid) > n//2 and (down + mid )> n//2:
        mediana = sp[i]
print(mediana)