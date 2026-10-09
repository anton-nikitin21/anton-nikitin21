sumi = []
for n in range(4, 1000):
    a = '>' + 11*'1'+'2' * n + 11 * '3'
    while '>1' in a or '>2' in a or '>3' in a:
        if '>1' in a:
            a = a.replace('>1', '222', 1)
        if '>2' in a:
            a = a.replace('>2', '3>', 1)
        if '>3' in a:
            a = a.replace('>3', '1>', 1)