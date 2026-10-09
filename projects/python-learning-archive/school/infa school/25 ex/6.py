def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return d
k=0
for i in range(700001,10**10):
    if len(div(i))==4:
        a=sorted(div(i))
        if a[-2]-a[1]<=15:
            print(i,a[-2]-a[1])
            k+=1
            if k==6:
                break
            