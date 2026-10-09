for n in range(250):
    b=bin(n)
    b=b + b[-1]
    if b.count('1')%2==0:
        b=b+'0'
    else:
        b=b+'1'
    if b.count('1')%2==0:
        b=b+'0'
    else:
        b=b+'1'
    r=int(b,2)
    if r >130:
        print(n,r)
        break