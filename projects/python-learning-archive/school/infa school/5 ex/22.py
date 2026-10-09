# for n in range(1,100):
n=11
b=a = bin(n)[2:]
c=(sum(map(int,b)))%2
b=b+str(c)
b=b+ (str(sum(map(int,a)))%2)
print(b)