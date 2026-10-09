from fnmatch import*
for i in range(169,10**9+1,169):
    if fnmatch(str(i),'123*567?'):
        print(i,i//169)