from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a == b :
        return 1
    if a > b or a == 30 :
        return 0
    if a < b:
        return f(a + 3, b) + f(a +5, b) + f(a * 2, b)

print(f(10, 20)*f(20,40))