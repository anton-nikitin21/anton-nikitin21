f = open('17_16383.txt')
a = [int(i) for i in f]
m21=max([i for i in a if abs(i)%100==21 and len(str(abs(i)))==5])
print(m21)

k=[]
for i in range(0,len(a)-1):
    if (abs(a[i])%100==21 and len(str(abs(a[i]))==5) + (abs(a[i])%100==21 and len(str(abs(a[i])))==5)) == 1:
        if a[i]**2+a[i+1]**2 >= m21**2:
            k.append(a[i]+a[i+1])

print(len(k),max(k))

    