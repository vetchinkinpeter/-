file = open('input4.txt')
lin = file.readline()
sp = list(map(int , lin.split()))
f = file.readline()
out = 0
if f == '+':
    for elem in sp:
        out += elem
elif f == '-':
    out = sp[0]
    for i in range(1,len(sp)-1):
        out -= sp[i]
elif f == '*':
    out = 1
    for elem in sp:
        out *= elem
outfile =  open('output4.txt', 'w')
outfile.write(str(out))