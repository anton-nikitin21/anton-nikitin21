B =[]
for i in range(18,53):
    B.append(i)

C =[]
for p in range(16,42):
    C.append(p)
    
for A in range(0,100):
    ok = True
    for x in range(0,100):
        F = (((x in (B)) <= (x == A)) and ((not(x in (C))) or (x  == A))) 
        if not F:
            ok = False
    if ok:
        print(A)
        
