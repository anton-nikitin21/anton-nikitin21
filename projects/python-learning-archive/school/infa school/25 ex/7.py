def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return d
k=0
for i in range(105_000_000,115_000_000+1):
    z=i
    while z%2==0:
        z=z//2
    if z**0.5 == int(z**0.5):
        a=div(z)
        if len(a)==5:
            print(i,max(a))