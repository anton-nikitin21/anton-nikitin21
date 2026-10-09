for A in range(0, 1000):
    OK = True 
    for x in range(0, 1000): 
        for y in range(0, 1000):
            F = (x>=27) or (2*x<3*y) or (A>(x+2)*(y-3))
            if not F:
                OK = False
                break
        if not OK: 
            break
    if OK:
        print(A)
            