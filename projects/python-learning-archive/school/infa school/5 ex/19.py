for n in range(100,1000):
    d=str(n)
    a=[int(d[0]+d[1]), int(d[1]+d[2])]
    r = max(a)-min(a)
    if r ==26:
        print(n,r)
    