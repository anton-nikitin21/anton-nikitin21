def cc(x,y):
    s=''
    while x>0:
        s = str(x%y) +s
        x=x//y
    return s

for n in range(1,200):
    b = cc((n),3)
    if n%3==0:
        b='1'+b+'02'
    else:
        b=b+cc((n%3*4),3)
    r=int(b,3)
    if r<199:
        print(n,r)