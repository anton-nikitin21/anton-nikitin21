for n in range(1,100):
    b1 =b =bin(n)[2:]
    b = b +b[-1]
    if b1.count('1')%2==0:
        b= b +'0'
    else:
        b=b+'1'
    if b1.count('1')%2==0:
        b= b +'0'
    else:
        b=b+'1'
    r = int(b,2)
    if r > 90:
        print(n,r)
        
    