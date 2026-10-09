from fnmatch import*
for i in range(17,10**9,17):
    if fnmatch(str(i),'12345?6?8'):
        print(i,i//17)