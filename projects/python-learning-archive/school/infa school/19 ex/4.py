def f(a, b, m):
    if a + b <= 72: return m % 2 == 0
    if m == 0: return 0
    h = [f(a - 3, b, m - 1), f(a, b - 3, m - 1), f((a + 1) // 2, b, m - 1), f(a, (b + 1) // 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else any(h)

print(19, [s for s in range(23, 100) if f(50, s, 2)]) 
