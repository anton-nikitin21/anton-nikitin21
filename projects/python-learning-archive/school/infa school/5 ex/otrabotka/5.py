for n in range(1000,9999):
    d = [int(d) for d in str(n)]
    a = d[0]*d[1]
    b=d[2] * d[3]
    if a<b:
        r= int(str(a)+str(b))
    else:
        r = int(str(b)+str(a))
    if r == 1214:
        print(n,r)