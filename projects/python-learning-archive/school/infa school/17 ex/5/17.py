f=open('17_6360.txt')
a = [int(i) for i in f]
M7 = min([i for i in a if abs(i)%10==7])


k=[]
for i in range(0,len(a)-1):
    if (abs(a[i])%10 == abs(a[i+1])%10):
        if (a[i]%7==0) + (a[i+1]%7==0) ==1:
            if (a[i]**2 + a[i+1]**2) <= M7**2:
                k.append(a[i]**2+a[i+1]**2)
            
print(len(k),max(k))