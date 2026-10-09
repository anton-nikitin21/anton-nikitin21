from math import*
k = 261
for N in range(1,1000):
    i = ceil(log2(N))
    I = ceil(i*k/8)
    if 252500* I > 31 *1024 *1024:
        print(N)