from math import *

N=910
i=ceil(log2(N))
for k in range(10000, 0,-1):
    I=ceil(i*k/8)
    if I*1500<=780*1024:
        print(k)
        break
    