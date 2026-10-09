
import sys
sys.setrecursionlimit(30000)
from math import*

def f(n):
    if n>=5000:
        return factorial(n)
    if n>=1 and n<5000:
        return 2*f(n+1)/(n+1)
    
print(1000*f(7)/f(4))