k = 0

def F(n):
    if n <= 15:
        return (n * n + 11)
    if n > 15 and n % 2 == 0:
        return F(n//2) + n**3 - 5 * n
    if n > 15 and n % 2 !=0:
        return F(n - 1) + 2 * n + 3

for n in range(1, 1001):
    if str(F(n)).count('6') >= 3:
        k += 1
print(k)