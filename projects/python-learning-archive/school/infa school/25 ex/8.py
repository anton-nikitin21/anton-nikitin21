def f(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)==2:
        return True
    else:
        return False
    
def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return d
    
for i in range(113_000_000,114_000_000+1,2):
    a=i//2
    if a**0.5== int(a**0.5):
        b=int(a**0.5)
        if f(b):
            c=sorted(div(b))
            print(i,c[1]*2)
            