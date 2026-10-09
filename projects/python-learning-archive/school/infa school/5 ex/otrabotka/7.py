# for n in range(100,1000):
#     d=[int(d) for d in str(n)]
#     d=sorted(d)
#     if d[0]==0 and d[1]==0:
#         MM = str(d[2])+str(d[1])
#         MN= str(d[2])+str(d[1])
#     elif d[0]==0:
#         MM = str(d[2])+str(d[1])
#         MN = str(d[1]) + str(d[2])
#     else:
#         MM= str(d[2])+str(d[1])
#         MN = str(d[0])+str(d[1])
#     if MN[0] == '0':
#         MN=MN[1:]
#     r = int(MM) - int(MN)
#     if r == 5:
#         print(n,r) 

def cc10(x):
    s=''
    d='0123456789abcdefghijklmnopqrst'
    while x>0:
        s=d[x%19]+s
        x=x//19
    return s
k=[]
for n in range(100_000,999999+1):
    b=cc10(n)
    
    b=b.replace('b','5').replace('c','5').replace('d','5').replace('f','5').replace('g','5').replace('h','5')
    b=cc10((n%19))+ b
    b=b[-2:] + b[:-2]
    
    b=b.replace('b','5').replace('c','5').replace('d','5').replace('f','5').replace('g','5').replace('h','5')
    b=b[-2:] + b[:-2]
    r=int(b,19)
    if sum(map(int,str(r)))%7==0:
        k.append(r)
print(max(k))
