import sys
sys.setrecursionlimit(3000)
k=0
def F(n):
    if n <= 18:
        return n+3
    if n>18 and n%3==0:
        return (n//3)*F(n//3)+n-12
    if n>18 and n%3!=0:
        return F(n-1)+n**2+5
    
for n in range(1, 1001):
    x=F(n)
    if all(int(d) % 2 == 0 for d in str(x)):
        k += 1
print(k)