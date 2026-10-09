for n in range(1,13):
    b=bin(n)[2:]
    if int(b)%2==0:
        b='10' + b  
    else:
        b= '1' + b + '01'
    r=int(b,2)
    print(n,r)