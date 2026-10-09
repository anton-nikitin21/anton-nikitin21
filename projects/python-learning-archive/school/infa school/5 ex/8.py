a=[]
for n in range(1,100):
    b = bin(n)[2:]
    if sum(map(int,b))%2==0:
        b = '10' + b[2:]+'0'
    else:
        b = '11' + b[2:] +'0'
    r=int(b,2)
    if r>=16:
        a.append(r)
        print(n,r)
print(min(a))