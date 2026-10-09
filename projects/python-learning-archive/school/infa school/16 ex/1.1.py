import sys
sys.setrecursionlimit(2100)

def F(n):
    if n == 0:
        return 1
    if n==1:
        return 3
    if n==2:
        return 2
    if n>2:
        return F(n-1)*F(n-3)

print(F(7))