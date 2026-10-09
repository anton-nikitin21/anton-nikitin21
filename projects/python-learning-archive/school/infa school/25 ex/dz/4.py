from fnmatch import*

def f(j):
    d=set()
    for i in range(1,int(j**0.5)+1):
        if j%i==0:
            d.add(i)
            d.add(j//i)
    return d

for j in range(0,10**6):
    if fnmatch(str(j),'?6*6*?6'):
        if j%6==0 and j%7==0 and j%8==0:
            print(j,sum(f(j)))
