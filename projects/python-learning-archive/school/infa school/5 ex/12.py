for n in range(1,100):
    b = bin(n) [2:]
    if len(b)%2==0:
        b = b[: len (b)//2] + '1' + b[len(b)//2:]
    r = int(b,2)
    if r<=26:
        print(n,r)