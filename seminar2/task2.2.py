st = str(input())
n = int(st[0])
st = st[2:]
st1 = ""
lenn = len(st)
for i in range(lenn//n):
    st1 = st1 + st[i*n +n : i*n :-1]

print(st1)