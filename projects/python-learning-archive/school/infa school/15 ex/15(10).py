def dell(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

def dell1(n, m):
    if n % m != 0:
        return 1
    else:
        return 0

for A in range(1,1000):
    OK=True
    for x in range(1,1000):
    
        F=(dell(x,14) <= dell1(x,4)) or (x+A>=200)
        if not F:
            OK= False
            break
    if OK:
        print(A)
        break
            