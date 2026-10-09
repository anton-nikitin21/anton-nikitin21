import sys
sys.setrecursionlimit(2000)

def F(n):
    if n>400:
        return n**n
    if n<=400:
        return n+6+F(n+12)
print(F(72)-F(108))