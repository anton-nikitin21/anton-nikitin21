# s=82*'8'
# while '1111' in s or '8888' in s:
#     if '1111' in s:
#         s=s.replace('1111','8',1)
#     else:
#         s=s.replace('8888','11',1)
# print(s)


# from itertools import *

# k = 0
# for j in range(2, 7): # кол-во двоек
#     for i in set(permutations('1' * 5 + '2' * j)):
#         s = ''.join(i)
#         if '111' not in s and '22' not in s:
#             k += 1
# print(k)