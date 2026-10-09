f = open('17_4705.txt')
a = [int(i) for i in f]
M3 = -10000
for i in a:
    if abs(i) % 10 == 3:
        M3 = max(M3, i)
# M3 = []
# for i in a:
#     if abs(i) % 10 == 3:
#         M3.append(i)
# print(max(M3))

# M3 = max([i for i in a if abs(i) % 10 == 3])
# print(M3)
k = []
for i in range(0, len(a) - 1):
    if (abs(a[i]) % 10 == 3) + (abs(a[i + 1]) % 10 == 3) == 1:
        if a[i] ** 2 + a[i + 1] ** 2 >= M3 ** 2:
            k.append(a[i] ** 2 + a[i + 1] ** 2)
print(len(k), max(k))
    