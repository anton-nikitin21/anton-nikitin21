sumi = []
c=0
for n in range(123456794, 678901235):
    a = '1' * n
    while '111' in a:
        a = a.replace('111', '2', 1)
        a = a.replace('222', '11', 1)
        a = a.replace('1', '2', 1)
        if a.count('1') == 1:
            break
        else:
            c+=1 

print(c)