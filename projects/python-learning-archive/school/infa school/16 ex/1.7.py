import sys
sys.setrecursionlimit(2500)

def F(n):
    if n<=3:
        return 3
    if n>3 and n%2==0:
        return F(n//2)+5
    if n>3 and n%2!=0:
        return F(n-1)-F(n-2)
print(F(20))
    