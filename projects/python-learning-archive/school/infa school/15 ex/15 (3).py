def dell(n, m):
    return n % m ==0
B= [70,71,72,73,74,75,76,77,78,79,80]
n=0
    
for A in range(1,10000):
    flag = True
    for x in range(1,10000):
        F=(dell(x, 12) and (x in (B)) and (not (dell(x,A))))
        if F:
            flag = False
            break
    if flag:    
        n+=1
print(n)
        
        