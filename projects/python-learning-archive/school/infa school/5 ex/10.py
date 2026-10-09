def cc(x):
    s=''
    d='0123456789ab'
    while x>0:
        s = d[x%12] +s
        x=x//12
    return s
z=[]
for n in range(12,500):
    b=cc(n)
    if n%12==0:
        b=b+b[-2]+b[-1]
    else:
        b=b+cc(n%12*9)
    r=int(b,12)
    if r>300:
        z.append(r)
print(min(z))

