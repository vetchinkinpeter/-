sp = list(map(int , input().split()))
for i in range (len(sp)) :
    if sp.count(sp[i]) == 1:
        print(sp[i])