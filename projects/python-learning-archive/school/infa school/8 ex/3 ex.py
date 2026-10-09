from itertools import*
c=0
n=0
for i in product('ЕЛОПРСТ',repeat= 5):
    f= ''.join(i)
    n+=1
    if f[-1] in 'ЕО' and f.count('П') + f.count('Р') + f.count('С') + f.count('Т') + f.count('Л') <=3 and n%2==0:
        c +=1
print(c)