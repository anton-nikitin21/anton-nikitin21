k=0
for i in range(1_000_001,10*9+1):
    d=set()
    for j in range(2,int(i*0.5)+1):
        if i%j == 0:
            d.add(j)
            d.add(i//j)
        if len(d)>0:
            M=min(d)+max(d)
            if M%10 == 6:
                print(i,M)
                k+=1
        if k==5:
            break