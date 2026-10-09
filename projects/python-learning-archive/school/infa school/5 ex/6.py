k=0
for n in range(1,100):
    b = bin(n)[2:]
    if sum(map(int,b))%2==0:
        b = b +'0'
    else:
        b=b+'1'
    if sum(map(int,b))%2==0:
        b = b +'0'
    else:
        b=b+'1'
    r= int(b,2)
    if 210<=r<=260:
        k+=1
print(k)
