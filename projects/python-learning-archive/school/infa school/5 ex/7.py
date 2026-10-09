a=[]
for n in range(1,100):
    b = bin(n)[2:]
    if n%2!=0:
        b='1'+b+'11'
    else:
        b='11' + b +'00'
    r=int(b,2)
    if r <127:
        a.append(r)
        print(n,r)
print(max(a))