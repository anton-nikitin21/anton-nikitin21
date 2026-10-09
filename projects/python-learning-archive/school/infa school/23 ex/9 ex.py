from functools import lru_cache

@lru_cache(None)
def f(x, end):
    if x == end:
        return 1
    if x > end or x == 100:
        return 0
    s = 0
    if x % 10 != 0:
        s += f(x + x % 10, end)
    if x % 68 != 0:
        s += f(x + x % 68, end)
    s += f(x**2, end)
    return s

print(f(2, 68) * f(68, 680))