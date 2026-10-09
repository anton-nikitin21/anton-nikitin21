def pos(n, m):
    if n-m > 0:
        return True
    else:
        return False

for A in range(0,1000):
    flag = True
    for x in range(0,1000):
        for y in range(0,1000):
            f=(not pos(x+y,73) or not pos(37,x-y) or pos(y,A))
            if not f:
                flag = False
                break
        if flag == False:
            break
    if flag:
        print(A)
            
        