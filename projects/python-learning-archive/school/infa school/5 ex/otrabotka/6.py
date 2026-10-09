for n in range(100,999+1):
    d = [int(d) for d in str(n)]
    a = d[0]*d[1]
    b= d[1]*d[2]
    if a > b:
        r=(str(a)+str(b))
    else:
        r=(str(b)+str(a))
    if int(r) == 240:
        print(n,r)
    