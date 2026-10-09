def cc (x):
    s=''
    while x>0:
        s = str(x%3) + s
        x=x//3
    return s

for n in range(1,250):
    b=cc(n)
    b=b+ str(n%3)
    r=int(b,3)
    print(r)
       