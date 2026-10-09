from itertools import*
a=set()
k=0
for i in product('БЕНРСЕЬЯ',repeat = 5):
    s= ''.join(i)
    k+=1
    if k %2==0 and 'Р' == s[0] and 'Ь' not in s :
        a.add(k)
print(max(a))
        
    
    
    
