def dell(n,m):
    if n%m==0:
        return 1
    else:
        return 0
    
for A in range(1,100):
    ok = True
    for x in range(1,100):
        F=not(dell(x,A)) <= (dell(x,14) >= (dell(x,4)))
        if not F:
            ok=False
            break
            
    if ok:
        print(A)
        break