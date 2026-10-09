# print('w,x,y,z,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=((x==(not(y))) or (x==(not(z)))) and w and (y <= z)
#                 if F:
#                     print(w,x,y,z,F)



# for n in range(1,150):
#     b=n-(n%8)+(n%2)
#     b=bin(b)[2:]
#     b=b + str(sum(map(int,b))%2)
#     b=b + str(sum(map(int,b))%2)
#     r=int(b,2)
#     if r>90:
#         print(n,r)

# b='11100'
# b=sum(map(int,b)) + (sum(map(int,b))%2)
# print(b)


# from turtle import*
# tracer(0)
# screensize(5000,5000)
# r=15

# rt(60)
# for i in range(4):
#     fd(8*r)
#     rt(120)
#     fd(4*r)
#     rt(240)

# rt(120)
# fd(2*r)
# rt(90)
# fd(16*(3**0.5)*r)
# rt(90)
# fd(2*r)

# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(4,'red')
        
# update()
# mainloop()


# from itertools import*
# k=0
# for x in product('0123',repeat=5):
#     s=''.join(x)
#     if s[0]!='0':
#         if s.count('3')==1:
#             if '30' not in s and '03' not in s:
#                 k+=1
# print(k)


# from math import*
# i=ceil(log2(10+100))

# for k in range(1,520):
#     I=ceil(k*i/8)
#     if 1800*I <= 720 * 1024:
#         print(k)


# 467
# 468


# s=70*'1'
# while '1111' in s or '2222' in s:
#     if '1111' in s:
#         s=s.replace('1111','22',1)
#     else:
#         s=s.replace('2222','11',1)
# print(s)



