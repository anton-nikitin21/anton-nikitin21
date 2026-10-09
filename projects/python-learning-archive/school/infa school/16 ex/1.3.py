import sys
sys.setrecursionlimit(2100)

def F(n):
    if n <=10:
        return n
    if 10<n<=36:
        return n//4+F(n-10)
    if n >36:
        return 2*F(n-5)
print(F(100))
    