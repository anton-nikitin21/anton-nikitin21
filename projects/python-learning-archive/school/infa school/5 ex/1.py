from itertools import*
a = 0
x = 0
for i in product('ЕЛОПРСТ', repeat = 5):
    s = ''.join(i)
    s = s.replace('Е', '*')
    s = s.replace('О', '*')
    s = s.replace('П', '-')
    s = s.replace('Р', '-')
    s = s.replace('С', '-')
    s = s.replace('Т', '-')
    s = s.replace('Л', '-')
    a += 1
    if a % 2 != 0 and s[-1] == '*' and s.count('-') <= 3:
        x += 1
print(x)