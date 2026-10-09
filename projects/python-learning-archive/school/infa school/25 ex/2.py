# from fnmatch import*
# for i in range(7777,10**9,7777):
#     if fnmatch(str(i), '???????77'):
#         s=str(i)
#         if int(s[0])%2==0 and int(s[1])%2!=0 and int(s[2])%2==0 and int(s[3])%2==0 and int(s[4])%2!=0 and int(s[5])%2==0 and int(s[6])%2!=0:
#             print(i,i//7777)
            
            
            
            
# from fnmatch import*
# for i in range(17,10**9,17):
#     if fnmatch(str(i),'12345?6?8'):
#         print(i,i//17)


from fnmatch import*
for i in range(141,10**8,141):
    if fnmatch(str(i),'1234*7'):
        print(i,i//141)