k=0
for n in range (100,1000):
    d = str(n)
    a = [d[0]+d[1], d[0]+d[2], d[1]+d[0], d[1]+d[2], d[2]+d[0], d[2]+d[1]]
    a = [int(x) for x in a if x [0]!='0']
    r = max(a) - min (a)
    if r==35:
        k+=1
print(k)