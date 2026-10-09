c=0
for a in range(1,1000):
    ok=True
    for x in range(1,1000):
        f=(x%12==0) and (70<=x<=80) and (x%a!=0)
        if f:
            ok=False
            break
    if ok:
        c+=1
print(c)