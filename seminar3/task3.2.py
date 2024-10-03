def rec(n):
    sp = []
    flag = 0
    if n == 1:
        return 'ГОЙДА'
    for i in range(2,n):
        if n % i == 0:
            sp1 = rec(i)
            sp2 = rec(n//i)
            for elem in sp1:
                if elem not in sp:
                    sp.append(elem)
            for elem in sp2:
                if elem not in sp:
                    sp.append(elem)
            flag = 1
            break

    if flag == 0:
        sp.append(n)
        return sp
    else:
        return sp
n = int(input())
print(rec(n))




