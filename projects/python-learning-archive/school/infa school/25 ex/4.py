k=0
for i in range(850_001,10**7+1):
    d=set()
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            d.add(j)
            d.add(i//j)
    if len(d)>0:
        F=max(d)-min(d)
        if F!=0 and F%13 == 0:
            print(i,F)
            k+=1
            if k==6:
                break