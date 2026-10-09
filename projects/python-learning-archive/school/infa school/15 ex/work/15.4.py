def mod(m,n):
    return m%n

for A in range(1,1000):
    Ok = True
    for x in range(1,1000):
        F=(((mod(x,4)!=3) or (mod(x,6)!=1)) <= (mod(x,36)!=A))
        if not F:
            Ok =False
            break
    if Ok:
        print(A)
        break