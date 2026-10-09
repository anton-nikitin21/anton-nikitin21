sumi = []
for n in range(4, 10000):
    a = '5' + '2' * n
    while '72' in a or '522' in a or '2222' in a:
        if '72' in a:
            a = a.replace('72', '2', 1)
        if '522' in a:
            a = a.replace('522', '27', 1)
        if '2222' in a:
            a = a.replace('2222', '5', 1)
    if sum([int(x) for x in a])==63:
        print(n)
        break