f=open('17_17611.txt')
a = [int(i) for i in f]

MX = max([i for i in a if abs(i)%10==7 and len(str(abs(i)))==4])
print(MX)

k=[]
for i in range(0,len(a)-2):
    if (abs(a[i])%10==7 and len(str(abs(a[i])))==4) + (abs(a[i+1])%10==7 and len(str(abs(a[i+1])))==4) + (abs(a[i+2])%10==7 and len(str(abs(a[i+2])))==4) == 2:
        if (a[i] + a[i+1] + a[i+2]) > MX:
            k.append(a[i]+a[i+1]+a[i+2])
            
print(len(k),max(k))