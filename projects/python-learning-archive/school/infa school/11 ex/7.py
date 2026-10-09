#20
from math import*
dr = ceil(log2(31*12*601)) *6
n=12*4
adr= ceil(log2(32))
for k in range(1,1000):
    I = adr * k
    z = I + n +dr
    z = ceil(z/8)
    if I * 1316 >= 27 *1024:
        print(k)