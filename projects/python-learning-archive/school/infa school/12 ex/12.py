sumi = []
for n in range(4, 10000):
    a = '8' + '4' * n
    while '11' in a or '444' in a or '8888' in a:
        if '11' in a:
            a = a.replace('11', '4', 1)
        if '444' in a:
            a = a.replace('444', '88', 1)
        if '8888' in a:
            a = a.replace('8888', '1', 1)
    x = a.count('1') * 1 + a.count('4') * 4 + a.count('8') * 8
    sumi.append(x)
print(max(sumi))
