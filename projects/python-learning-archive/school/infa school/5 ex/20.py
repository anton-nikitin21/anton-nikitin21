k=0
for n in range(1,1000):
    a = [int(d) for d in str(n)]
    s1 = sum(d for d in a if d%2==0)
    s2=0
    for i in range(len(a)):
        if (i+1)%2:
            s2+=a[i]
    r = abs(s2-s1)
    if r ==7:
        print(n,r)