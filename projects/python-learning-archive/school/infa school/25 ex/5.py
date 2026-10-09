def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i != 9 and i % 10 == 9:
                d.add(i)
            if x // i != 9 and x // i % 10 == 9:
                d.add(x // i)
    if len(d) > 0:
        return min(d)
    else:
        return -1
    

k = 0
for i in range(800001, 1000000000):
    if f(i) != -1:
        print(i, f(i))
        k += 1
        if k == 5:
            break