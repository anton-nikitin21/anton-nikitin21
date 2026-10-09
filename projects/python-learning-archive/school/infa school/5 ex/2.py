d=[]
for n in range(1,1000):
    n2= bin(n)[2:]
    if n %2==0:
        s=''
        for i in n2:
            if i == '1':
                s+= '11'
            else:
                s+= i 
    else:
        s = n2.replace('0','00')
    r = int(s,2)
    if r<70 and r!=n:
        d.append(n)
print(max(d))
