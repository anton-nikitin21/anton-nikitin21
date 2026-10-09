from itertools import*

k=0
for i in product('012345678',repeat =7):
    s= ''.join(i)
    if int(s[0]) % 2 ==0 and int(s[-1]) % 3 != 0 and '6' in s and s[0] != '0':
        k+=1
        
print(k)
        