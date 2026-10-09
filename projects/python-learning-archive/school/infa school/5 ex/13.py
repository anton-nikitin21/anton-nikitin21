for n in range(1000,9999):
    d = [int(d) for d in str(n)]
    a = d[0]+d[2]
    b=d[1] + d[3]
    if a<b:
        r= int(str(a)+str(b))
    else:
        r = int(str(b)+str(a))
    if r == 1315:
        print(n,r)