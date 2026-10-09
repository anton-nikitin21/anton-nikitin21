def f(a, b, k1, k2):
    if a == b and k2 > k1:
        return 1
    if a > b or (a==b and k2 <= k1):
        return 0
    if a < b:
        return f(a + 3, b, k1 + 1, k2) + f(a * 2, b, k1, k2 + 1) + f(a * 7, b, k1, k2 + 1)

print(f(2, 472, 0, 0))