import sys
sys.setrecursionlimit(100000)

def F(n):
    if n == 1:
        return 1
    if n>1:
        return (4*n-3)*F(n-1)

print((int(F(5168))/11+int(F(5166)))/int(F(5165)))