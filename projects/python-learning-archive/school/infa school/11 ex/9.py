from math import*
i=ceil(log2(10+52+963))
for k in range(1,2000):
    I=ceil(i*k/8)
    if 693*1024/2000 >= I:
        print(k)
