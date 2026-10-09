def cc(x):
    s=''
    while x>0:
        s=str(x%3)+s
        x=x//3
    return s

for n in range(1,250):
    b=cc(n)
    if n%3==0:
        b=b+b[-2::]
    else:
        z=sum(map(int,b))
        c=cc(z)
        b=b+c
    r=int(b,3)
    if r>220:
        print(n,r)
# s='123456'
# print(s[-2::]) 56