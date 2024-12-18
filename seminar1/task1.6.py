file = open('input6.txt')
lin = file.readline()
sp = list(map(int , lin.split()))
f = file.readline()
if f[0] == '+':
    f = '+'
if f[0] == '-':
    f = '-'
if f[0] == '*':
    f = '*'
b = int(file.readline())
sp2 = []
for i in range(len(sp)):
    nst = str(sp[i])
    N10 = 0
    for i in range(len(nst)):
        N10 += int(nst[-(i + 1)]) * b ** i
    sp2.append(N10)
out = 0
if f == '+':
    for elem in sp2:
        out += elem
elif f == '-':
    out = sp2[0]
    for i in range(1,len(sp2)):
        out -= sp2[i]
elif f == '*':
    out = 1
    for elem in sp2:
        out *= elem
out2 = ''
while out > 0:
    out2 += str(out % b)
    out = out//b
out3 = ''
for i in range(len(out2)):
    out3 += out2[-i-1]
outfile =  open('output6.txt', 'w')
outfile.write(str(out3))