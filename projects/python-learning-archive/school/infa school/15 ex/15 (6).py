
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = ((x | 42 > 64) and (x | 34 <= 102) <= (not(x | A < 70)))
        if not f:
            flag = False
            break
    if flag == True:
        print(A)
        break
    
