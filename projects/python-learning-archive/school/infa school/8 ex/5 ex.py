# from itertools import*
# k=0
# for x in product('ЛТ','ЛЕТО','ЛЕТО','ЛЕТО'):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('км','кума','кума','кума','уа'):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('abc','abc','abc','abc','abcx'):
#     s=''.join(x)
#     k+=1
# print(k)

# from itertools import*
# k=0
# for x in product('эюя','абвг','абвг','абвг','эюя'):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('крот',repeat = 6):
#     s=''.join(x)
#     if s.count('о')==1:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('АНИМЕ',repeat=4):
#     s=''.join(x)
#     k+=1
# for t in product('АНИМЕ',repeat=5):
#     s=''.join(x)
#     k+=1
# for z in product('АНИМЕ',repeat=6):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('ЛЕТО',repeat=4):
#     s=''.join(x)
#     if s.count('Е')>=1:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('ЖИРАФ',repeat=5):
#     s=''.join(x)
#     if s.count('Ж')==1 and s[0]!='Ф' and s[-1]!='Р':
#         k+=1
# print(k)


# from itertools import*
# k=0
# # for x in permutations('КАЛИЙ',5):
# for x in product('КАЛИЙ',repeat=5):
#     s=''.join(x)
#     if s[0]!='Й' and 'ИА' not in s:
#         if s.count('К')==1 and s.count('А')==1 and s.count('Л')==1 and s.count('И')==1 and s.count('Й')==1:
#             k+=1 
# print(k)


# from itertools import*
# k=0
# for x in set(permutations('КОЛУН',5)):
#     s=''.join(x)
#     s=s.replace('Л','К').replace('Н','К').replace('У','О')
#     if 'КК' not in s and 'ОО' not in s:
#         k+=1
# print(k)
    
# from itertools import*
# k=0
# for x in permutations('КОЛУН',5):
#     s=''.join(x)
#     if 'ОУ' not in s and 'УО' not in s:
#         if 'КЛ' not in s and 'КН' not in s and 'ЛК' not in s and 'ЛН' not in s and 'НК' not in s and 'НЛ' not in s:
#             k+=1
# print(k)
    

# from itertools import*
# k=0
# for x in permutations('ПЕСКАРЬ',7):
#     s=''.join(x)
#     if s[0]!='Ь' and 'ЬЕ' not in s and 'ЬА' not in s and 'ЬР' not in s:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in set(permutations('АССАСИН',7)):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in permutations('01234567',6):
#     s=''.join(x)
#     if s[0]!='0':
#         s=s.replace('0','2').replace('4','2').replace('6','2')
#         s=s.replace('3','1').replace('5','1').replace('7','1')
#         if '22' not in s and '11' not in s:
#             k+=1
# print(k)
            

# from itertools import*
# k=0
# for x in product('01234567',repeat=4):
#     s=''.join(x)
#     # if (s[0]=='2' or s[0]=='4' or s[0]=='6')
#     if s[0] in '246':
#         if s[0]>=s[1]>=s[2]>=s[3]:
#             k+=1
# print(k)


# from itertools import*
# k=0
# for x in product(sorted('АКРУ'),repeat=5):
#     s=''.join(x)
#     k+=1
#     if k==150:
#         print(k,s)


# from itertools import*
# k=0
# for x in product(sorted('АОУ'),repeat=5):
#     s=''.join(x)
#     k+=1
#     if s=='УАУАУ':
#         print(k)


# from itertools import*
# k=0
# last=0
# for x in product(sorted('МАНГУСТ'),repeat=6):
#     s=''.join(x)
#     k+=1
#     if s[0]!= 'У' and s.count('М')==2 and s.count('Г')<=1:
#         last=k
# print(last)


# from itertools import*
# k=0
# l=0
# for x in product(sorted('КОМПЬЮТЕР'),repeat=5):
#     s=''.join(x)
#     k+=1
#     if k%2!=0 and s[0]!='Ь' and s.count('К')==2:
#         l+=1
# print(l)



# from itertools import *
# k = 0
# for i in permutations('0123456789ABCDE', 8):
#     s = ''.join(i)
#     if s[0] != '0' and int(s, 15) <= 855_000_000:
#         k += 1
# print(k)





# k=0
# for a in 'ЛТ':
#     for b in 'ЛЕТО':
#         for c in 'ЛЕТО':
#             for d in 'ЛЕТО':
#                 k+=1
# print(k)

# from itertools import*
# k=0
# for x in product('ЛТ','ЛЕТО','ЛЕТО','ЛЕТО'):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('КМ',"КУМА","КУМА","КУМА","УА"):
#     s=''.join(x)
#     k+=1
# print(k)

# from itertools import*
# k=0
# for x in product('ABC','ABC','ABC','ABC','ABCX'):
#     s=''.join(x)
#     k+=1
#     print(s)
    
# print(k)



# from itertools import*
# k=0
# for x in product('КРОТ',repeat=6):
#     s=''.join(x)
#     if s.count('О')==1:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('КАНТ',repeat=6):
#     s=''.join(x)
#     if s.count('К')==2:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in product('ЗЕРКАЛО',repeat=6):
#     s=''.join(x)
#     if s.count('К')==1 and s.count('А')==3:
#             k+=1
# print(k)



# from itertools import*
# k=625
# z=3125
# l=15625
# j=0
# for x in product('АНИМЕ',repeat=6):
#     s=''.join(x)
#     j+=1
# print(k+z+l)




# from itertools import*
# k=0
# for x in product('БЕРКЛИЙ',repeat=4):
#     s=''.join(x)
#     if s[0]!='Й':
#         if s.count('Е')+s.count('И')>=1:
#             k+=1
# print(k)




# from itertools import*
# k=0
# for x in product('ЖИРАФ',repeat=5):
#     s=''.join(x)
#     if s[0]!="Ф" and s[-1]!='Р':
#         if s.count('Ж')==1:
#             k+=1
# print(k)




# from itertools import*
# k=0
# for x in permutations('КАЛИЙ',5):
#     s=''.join(x)
#     if s[0]!='Й' and 'ИА' not in s:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in permutations('КОЛУН'):
#     s=''.join(x)
#     s=s.replace('К','*').replace('Л','*').replace('Н','*')
#     s=s.replace('У','О')
#     if 'ОО' not in s and '**' not in s:
#         k+=1
# print(k)


# from itertools import*
# k=0
# for x in permutations('ПЕСКАРЬ',7):
#     s=''.join(x)
#     if s[0]!='Ь' and 'ЬЕ' not in s and 'ЬА' not in s and 'ЬР' not in s:
#         k+=1
# print(k)





# from itertools import*
# k=0
# for x in set(permutations('ассасин',7)):
#     s=''.join(x)
#     k+=1
# print(k)


# from itertools import*
# k=0
# for x in permutations('01234567',6):
#     s=''.join(x)
#     if s[0]!='0':
#         s=s.replace('2','0').replace('4','0').replace('6','0')
#         s=s.replace('3','1').replace('5','1').replace('7','1')
#         if '00' not in s and '11' not in s:
#             k+=1
# print(k)
        
        
        
# from itertools import*
# k=0
# for x in product('01234567',repeat= 4):
#     s=''.join(x)
#     if s[0] in '246':
#         if int(s[0])>=int(s[1])>=int(s[2])>=int(s[3]):
#             k+=1
#             print(s)
# print(k)



# from itertools import*
# k=0
# for x in product(sorted('АОУ'),repeat=5):
#     s=''.join(x)
#     k+=1
#     if s=='УАУАУ':
#         print(k,s)



# from itertools import*
# k=0
# last=0
# for x in product(sorted('МАНГУСТ'),repeat=6):
#     s=''.join(x)
#     k+=1
#     if s[0]!='У' and s.count('М')==2 and s.count('Г')<=1:
#         last=k
# print(last)


# from itertools import*
# k=0
# z=0
# for x in product(sorted('КОМПЬЮТЕР'),repeat=5):
#     s=''.join(x)
#     k+=1
#     if k%2!=0 and s[0]!='Ь' and s.count('К')==2:
#         z+=1
# print(z)



# from itertools import*
# k=0
# for x in permutations('0123456789',4):
#     s=''.join(x)
#     if s[0]!='0':
#         s=s.replace('2','0').replace('4','0').replace('6','0').replace('8','0')
#         s=s.replace('3','1').replace('5','1').replace('7','1').replace('9','1')
#         if '11' not in s and '00' not in s:
#             k+=1
# print(k)



