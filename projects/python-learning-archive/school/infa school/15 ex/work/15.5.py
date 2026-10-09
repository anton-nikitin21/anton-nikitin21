def dell(n,m):
    return n%m==0
for A in  range(1,1000):
    Ok = True
    for x in range(1,1000):
        F=(dell(A,7) and (dell(240,x) <= ((not(dell(A,x))) <= (not(dell(780,x))))))
        if not F:
            Ok = False
            break
    if Ok:
        print(A)
        break