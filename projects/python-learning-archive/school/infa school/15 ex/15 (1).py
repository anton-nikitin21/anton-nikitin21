for A in range(0, 1000):
    OK = True 
    for x in range(0, 1000): 
        for y in range(0, 1000):
            F = (x < A) or (y < A) or (x + 2 * y > 50)
            if not F:
                OK = False
                break
        if not OK: 
            break
    if OK:
        print(A)
        break