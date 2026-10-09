f=open('')
a= [int(i) for i in f]
MM=min([i for i in a if abs(i)%19==0])

k=[]
for i in range(0,len(a)-1):
    if a[i]%MM==0 or a[i+1]%MM==0:
        k.append(a[i]+a[i+1])
print(len(k),max(k))