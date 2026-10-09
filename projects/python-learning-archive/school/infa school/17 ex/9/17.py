# f=open('')
# a = [int(i for i in f)]

# k=[]

# for i in range(0,len(a)-2):
#     if sum(map(abs(i)))+sum(map(abs(i+1)))+sum(map(abs(i+2))) == M4:
#         k.append(sum(map(abs(i)))+sum(map(abs(i+1)))+sum(map(abs(i+2))))
# print(len(k),max(k))




f=open('')
a= [int(i) for i in f]


def summ(x):
    return sum(map(int,str(x)))

z13=[i for i in a if i%13==0 ]
s13=summ(z13[12])

z25=[i for i in a if i%25==0 ]
s25=summ(z25[24])


k=[]
for i in range(0,len(a)-2):
    if len(str(a[i]))==3 or len(str(a[i+1]))==3 or len(str(a[i+2]))==3:
        if (summ(a[i])==s13) + (summ(a[i+1])==s13) + (summ(a[i+2])==s13) <=1:
            if (summ(a[i])==s25) + (summ(a[i+1])==s25) + (summ(a[i+2])==s25) >=2:
                k.append(a[i]+a[i+1] +a [i+2])
                

print(len(k),int(sum(k)/len(k)))