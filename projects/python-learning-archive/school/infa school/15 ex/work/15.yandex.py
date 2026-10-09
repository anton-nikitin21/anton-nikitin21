def dell(n, m):
    return n % m ==0
B= [70,71,72,73,74,75,76,77,78,79,80]
n=0
    
for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        F=((dell(x, A) and (dell(x,24)) and (not(dell(x,16))) ) <= (not (dell(x,A)))) 
        if not F:
            flag = False
            break
    if flag:    
        print(A)
        break
#print(n)
        
        