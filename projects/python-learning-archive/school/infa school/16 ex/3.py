F=[0]*5000
F[0]=1
F[1]=0
for n in range(2,5000):
    if n%2==0:
        F[n]=F[n//2]+1
        
    else:
        F[n]=F[n//2]
    if F[n]==10:
        break
print(n)