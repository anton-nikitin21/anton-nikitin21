from itertools import*
c = 0
for i in product('1234560', repeat = 6):
    f = ''.join(i)
    if f[0] != '0' and f.count('0') == 1:
        f = f.replace('2', '-')
        f = f.replace('4', '-')
        f = f.replace('6', '-')
        if '0-' not in f and '-0' not in f:
            c += 1
print(c)