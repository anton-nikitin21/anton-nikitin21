# def cc10(x):
#     s=''
#     d='0123456789abcdefghijklmnopqrstuvwxyz'
#     while x >0:
#         s=d[x%27] + s
#         x=x//27
#     return s
  
# z=2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
# c=cc10(z)
# #abcdefghijklmnopq
# v=c.count('a')+c.count('b')+c.count('c')+c.count('d')+c.count('e')+c.count('f')+c.count('g')+c.count('h')+c.count('i')+c.count('j')+c.count('k')+c.count('l')+c.count('m')+c.count('n')+c.count('o')+c.count('p')+c.count('q')
# print(v)




# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%8)+s
#         x=x//8
#     return s
# a=64**30+2**300-4
# b=cc(a)
# z=b.count('7')
# print(z)



# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%3)+s
#         x=x//3
#     return s
# a=2*27**7+3**10-9
# b=cc(a)
# print(b.count('0'))




# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%5)+s
#         x=x//5
#     return s
# for x in range(1,1000):
#     a=125**200-5**x+74
#     b=cc(a)
#     if b.count('4')==100:
#         print(x)
        
        
# def cc25(x):
#     s=''
#     d='0123456789abcdefghijklmnopqrstuvwxyz'
#     while x>0:
#         s=d[x%25]+s
#         x=x//25
#     return s
# a=3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
# b=cc25(a)
# print(b.count('0'))



# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%6)+s
#         x=x//6
#     return s
# for x in range(1,100):
#     a=36**17-6**x+71
#     b=cc(a)
#     if sum(map(int,b)) ==61:
#         print(x)


# for x in range(1,100):
#     a=3*(x+4)+3
#     b=3*4+3
#     c=33
#     if a-b==c:
#         print(x)


# for n in range(-50,100):
#     a=1*n**2+3*n+2
#     b=1*8+3
#     c=1*(n+1)**2+2*(n+1)+4
#     if a+b==c:
#         print(n)


# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%3)+s
#         x=x//3
#     return s
# for x in range(21,30):
#     b=cc(x)
#     if b[-2::] == '11':
#         print(x)



# def cc(x,y):
#     s=''
#     while x>0:
#         s=str(x%y)+s
#         x=x//y
#     return s

# for y in range(2,20):
#     print(y,cc(68,y))
        
        
        
        
# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%5)+s
#         x=x//5
#     return s
# k=0          
# for n in range(1,100000):
#     a=bin(n)[2:]
#     b=cc(n)
#     c=hex(n)[2:]
#     if len(a)>=5:
#         if len(b) <= 4:
#             if c[-1]=='c':
#                 k+=1
# print(k)


# for x in range(1,18):
#     a=9*17**4+7*17**3+5*17**2+9*17+x
#     b=3*17**4+x*17**3+1*17**2+0+8
#     if (a+b)%11==0:
#         print(x,(a+b)/11)#2


for x in range(1,16):
    for y in range(1,18):
        a=1*15**4+2*15**3+3*15**2+x*15+5
        b=6*17**3+7*17**2+y*17+9
        if (a+b)%131==0:
            print(a,b,(a+b)/131)