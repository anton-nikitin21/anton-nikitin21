def f(start, end, k1, k2,k3):
    if start == end and k1<2 and k2<2 and k3<2:
        return 1
    if start > end or k1>2 or k2>2 or k3>2:
        return 0
    if start < end:
        return f(start + 3, end, k1 + 1, k2) + f(start * 2, end, k1, k2 + 1) + f(start * 7, end, k1, k2 + 1)

print(f(2, 472, 0, 0))