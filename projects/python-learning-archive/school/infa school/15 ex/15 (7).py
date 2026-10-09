def dell(n, m):
    return n % m ==0
n=0
    
for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        F=(dell(x, 15) and (not(dell(x,21))) <= (not(dell(x,A)) or not(dell(x,15))))
        if F:
            flag = False
            break
    print(A)
    break
   
   
   
   # if flag:    
    #    n+=1
