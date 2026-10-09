def dell(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        f = (dell(x, 175) <= (not (dell(x, 25)))) or ((2 * x + A) >= 1780)
        if not(f):
            flag = False
            break
    if flag:
        print(A)
        break