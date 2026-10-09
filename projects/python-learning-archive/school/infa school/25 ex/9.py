def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return d

for k in range(1,100000):
    n = 750_000 +k
    s=div(n)
    f=0
    for i in s:
       if i % 2 == 0:
           f += 1
    if f%2 != 0:
        print(k,f)