from math import*
k=25
z=[]
i=ceil(log2(10+26+26+465))
I=ceil(k*i/8)
for d in range(1,10000):
    if 1500 * (I + d) <= 77 *1024:
        z.append(d)
print(max(z))