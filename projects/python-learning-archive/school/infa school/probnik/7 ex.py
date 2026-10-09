# print('w,x,y,z,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=not(x <= w) or (y<= z) or not(y)
#                 if not F:
#                     print(w,x,y,z,F)
            
        
        
# for n in range (101):
#     b=bin(n)[2:]
#     if sum(map(int,b))%2==0:
#         b='10' + b[2:]+'0'
#     else:
#         b= '11' + b[2:]+'1'
#     r=int(b,2)
#     if r>50:
#         print(n,r)




# from turtle import*
# tracer(0)
# screensize(5000,5000)
# r=15

# for i in range(9):
#     fd(22*r)
#     rt(90)
#     fd(6*r)
#     rt(90)
# up()
# fd(r)
# rt(90)
# fd(5*r)
# lt(90)
# down()
# for i in range(9):
#     fd(53*r)
#     rt(90)
#     fd(75*r)
#     rt(90)
    

# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot('4','red')

# update()
# mainloop()
        
        
# k=1024*960
# n=8192
# from math import*
# i=ceil(log2(n))
# I=k*i
# t=I/1_474_560
# for x in range(1,100):
#     if t*x <= 280:
#         print(x)


# from itertools import*
# k=0
# for x in product('01234567',repeat=5):
#     s=''.join(x)
#     if s[0]!='0' and s[0]!='1' and s[0]!='3' and s[0]!='5' and s[0]!='7' :
#         if s[-1]!='2' and s[-1]!='6':
#             if s.count('7') <=2:
#                 k+=1
# print(k)

# from math import*
# i=ceil(log2(10+52+458))
# for k in range(1000):
#     I=k*i
#     if 862*I <= 276*1024*8:
#         print(k)
# print((i*262*862)/8/1024)


# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%7)+s
#         x=x//7
#     return s


# for x in range(1,801):
#     z=7**1040+7**40-x
#     b=cc(z)
#     if b.count('0')==1002:
#         print(x)



# def f(x,y,a):
#     return (x>=a) or (y>=a) or (x*y<=200)

# for a in range(1,300):
#     if all(f(x,y,a)==1 for x in range(1,300) for y in range(1,300)):
#         print(a)


from math import*

k=640*780

for i in range(100):
    i1=ceil(log2(522))
    I=k*(i+i1)
    if I <= 900*1024*8:
        print(i)


