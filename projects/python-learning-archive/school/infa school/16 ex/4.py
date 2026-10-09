k=0
F=[0]*1001
for n in range(0,16):
    F[n]=n*n+11
    if str(F[n]).count('6') >= 3:
        k += 1
for n in range(15,1001):
    if n%2==0:
        F[n]=F[n//2]+n**3
    else:
        F[n]=F[n-1]+2*n+3
    if str(F[n]).count('6') >= 3:
        k += 1
print(k)