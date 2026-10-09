
for A in range(1, 1000):
    OK = True 
    for x in range(1, 1000): 
        for y in range(1, 1000):
            F = (x <= 19) or (y < (2*x+ A -50)) or (y > 17)
            if not F:
                OK = False
                break
        if not OK: 
            break
    if OK:
        print(A)
        break