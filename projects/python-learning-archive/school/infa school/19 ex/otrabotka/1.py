# def f(s,m):
#     if s>33: return m%2==0
#     if m==0: return 0
#     h=[f(s+1,m-1),f(s+2,m-1),f(s+3,m-1),f(s*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,34) if f(s,2)])
# print(20,[s for s in range(1,34) if not f(s,1) and f(s,3)])
# print(21,[s for s in range(1,34) if not f(s,2) and f(s,4)])


# def f(a,b,m):
#     if a+b >= 59: return m%2==0
#     if m==0:return 0
#     h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(2,53) if f(5,s,1)])
# print(10,[s for s in range(2,53) if not f(5,s,1) and f(5,s,3)])
# print(21,[s for s in range(2,53) if not f(5,s,2) and f(5,s,4)])


# def f(a,b,m):
#     if a+b>=68: return m%2==0
#     if m==0:return 0
#     h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a+b,b,m-1),f(a,b+a,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,60) if f(8,s,2)])
# print(20,[s for s in range(1,60) if not f(8,s,1) and f(8,s,3)])
# print(21,[s for s in range(1,60) if not f(8,s,2) and f(8,s,4)])



# def f(a,b,c,m):
#     if a+b+c>=73: return m%2==0
#     if m==0: return 0
#     h=[f(a+3,b,c,m-1),f(a,b+3,c,m-1),f(a,b,c+3,m-1),f(a+13,b,c,m-1),f(a,b+13,c,m-1),f(a,b,c+13,m-1),f(a+23,b,c,m-1),f(a,b+23,c,m-1),f(a,b,c+23,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,24) if f(2,s,2*s,2)])
# print(20,[s for s in range(1,24) if not f(2,s,2*s,1) and f(2,s,2*s,3)  ])
# print(21,[s for s in range(1,24) if not f(2,s,2*s,2) and f(2,s,2*s,4)  ])



# def f(s,m):
#     if s>=2163: return m%2==0
#     if m==0:return 0
#     h=[f(s+1,m-1),f(s*3,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,2163) if f(s,2)])
# print(20,[s for s in range(1,2163) if not f(s,1) and f(s,3)])
# print(21,[s for s in range(1,2163) if not f(s,2) and f(s,4)])


# def f(a,b,m):
#     if a+b<=20:return m%2==0
#     if m==0:return 0
#     h1=[f(a-1,b,m-1),f(a,b-1,m-1)]
#     if a%2==0:
#         h2=[f(a/2,b,m-1),f(a,b/2,m-1)] 
#     else: 
#         h2=[f(a//2+1,b,m-1), f(a,b//2+1,m-1)]
#     h=h1+h2
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(11,100) if f(10,s,2)])
# print(20,[s for s in range(11,100) if not f(10,s,1) and f(10,s,3)])
# print(21,[s for s in range(11,100) if not f(10,s,2) and f(10,s,4)])



# def f(s,m):
#     if s>=67: return m%2==0
#     if m==0: return 0
#     h=[f(s+1,m-1),f(s+3,m-1),f(s*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,67) if f(s,2)])
# print(20,[s for s in range(1,67) if not f(s,1) and f(s,3)])
# print(21,[s for s in range(1,67) if not f(s,2) and f(s,4)])

# def f(s,m):
#     if s<=15:return m%2==0
#     if m==0:return 0
#     h = []
#     if not any(s % k == 0 for k in range(2, 10)):
#         s -= 1
#     for k in range(2, 10):
#         if s % k == 0:
#             h.append(f(s - k, m - 1))
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(15,100) if f(s,2)])
# print(20,[s for s in range(15,100) if not f(s,1) and f(s,3)])
# print(21,[s for s in range(15,100) if not f(s,2) and f(s,4)])


# def f(s,m):
#     if s<=19: return m%2==0
#     if m ==0 :return 0
#     h=[f(s-3,m-1)]
#     if s%2==0:
#         h.append(f(s/2,m-1))
#     else:
#         h.append(f((s+3)//2,m-1))
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(20,100) if f(s,2)])
# print(20,[s for s in range(20,100) if  not f(s,1) and f(s,3)])
# print(21,[s for s in range(20,100) if  not f(s,2) and f(s,4)])






# def f(s, n):
#     if s < 20: return n == 0
#     if n == 0: return 0
#     h = [f(s - 10, n - 1), f(s // 2, n - 1)]
#     return all(h) if n % 2 != 0 else any(h)

# print(19, [s for s in range(31, 200) if f(s, 3) and not(f(s, 1))])
# print(20, [s for s in range(31, 200) if f(s, 4) and not(f(s, 2))])
# print(21, [s for s in range(31, 200) if f(s, 5) and not(f(s, 3)) and not(f(s, 1))])




# def f(s,m):
#     if s>33: return m%2==0
#     if m==0: return 0
#     h=[f(s+1,m-1),f(s+2,m-1),f(s+3,m-1),f(s*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,34) if f(s,2)]) 
# print(19,[s for s in range(1,34) if f(s,3) and not f(s,1)]) 
# print(21,[s for s in range(1,34) if f(s,4) and not f(s,2)]) '



# def f(s,m):
#     if s>=36 and s<=60: return m%2==0
#     if s>60: return m%2!=0
#     if m==0:return 0
#     h=[f(s+1,m-1),f(s*2,m-1),f(s*3,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,36) if f(s,2)])
# print(20,[s for s in range(1,36) if not f(s,1)and f(s,3)])
# print(21,[s for s in range(1,36) if not f(s,2)and f(s,4)])



# def f(a,b,m):
#     if a+b>=77: return m%2==0
#     if m==0: return 0
#     h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,70) if f(7,s,2)])
# print(20,[s for s in range(1,70) if not f(7,s,1) and f(7,s,3)])
# print(21,[s for s in range(1,70) if not f(7,s,2) and f(7,s,4)])







# def f(a,b,m):
#     if a*b>=63: return m%2==0
#     if m==0: return 0
#     h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,32) if f(2,s,2)])
# print(20,[s for s in range(1,32) if not f(2,s,1) and f(2,s,3)])
# print(21,[s for s in range(1,32) if not f(2,s,2) and f(2,s,4)])


# from itertools import*
# k=0
# for x in permutations('0123456789ABC',7):
#     s=''.join(x)
#     if s[0]!='0':
#         if '1B' not in s and '3B' not in s and '5B' not in s and '7B' not in s and '9B' not in s:
#             if 'B1' not in s and 'B3' not in s and 'B5' not in s and 'B7' not in s and 'B9' not in s:
#                 k+=1
           
# print(k)


# print('w,x,y,z,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=not((not(z<=y)) or (x==w) or x)
#                 if F:
#                     print(w,x,y,z,F)        



# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%7)+s
#         x=x//7
#     return s

# for n in range(1,250):
#     b=cc(n)
#     if sum(map(int,b))%2==0:
#         b=b+'555'
#     else:
#         b='33' +b + '6'
        
#     r=int(b,7)
#     if r<12717:
#         print(n,r)




# from turtle import*

# screensize(5000)
# tracer(0)
# lt(90)
# r=5
# for i in range(4):
#     fd(50*r)
#     lt(90)

# up()
# fd(50*r)
# lt(135)
# down()

# for i in range(2):
#     fd(102*r)
#     lt(120)
#     fd(182*r)
#     lt(60)
    
# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(3,'red')
        
# update()
# mainloop()



# from math import*

# i=ceil(log2(10**7))
# print(i)
# for k in range(100000,1000000):
#     I=k*i
#     if (I*10)/2100000 <= 3*60:
#         k




# from itertools import*
# k=0
# for x in permutations('0123456789ABC',7):
#     s=''.join(x)
#     if s[0]!='0':
#         if '1B' not in s and '3B' not in s and '5B' not in s and '7B' not in s and '9B' not in s:
#             if 'B1' not in s and 'B3' not in s and 'B5' not in s and 'B7' not in s and 'B9' not in s:
#                 k+=1
# print(k)




# from math import*
# k=25
# i = ceil(log2(52+10+20))
# I=ceil(k*i/8)
# print(I)
# for n in range(20000,21000):
#     if n*(I+30) <= 1*1024*1024:
#         print(n)




# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%7)+s
#         x=x//7
#     return s

# z=15*343**2031+7*49**1142-3*7**111+7**222-16809
# b=cc(z)
# a1=[x for x in b if int(x)%2==0]
# a2=[x for x in b if int(x)%2!=0]
# print(len(a1)-len(a2))


from math import*
def f(x,y,a):
    return (x**2 <= 136) or (y<4*x+a-70) or (2*y>51)

for a in range(0,1000):
    if all(f(x,y,a)==1 for x in range(0,3000) for y in range(0,3000)):
        print(a)



# import sys
# sys.setrecursionlimit(100000)

# def f(n):
#     if n>80000:
#         return 100
#     else:
#         return f(n+1)*n
    
# print(((f(50)//100)+f(53))/f(55))
        
# F=[0]*100000000

# for n in range(80002,10**10):
#     F[n]=100
#     for n in range(2,80001):
#         F[n]=F[n+1]*n
# print((F[50]/100+F[53])/F[55])


# from math import*
# def f(s,m):
#     if s<=23: return m%2==0
#     if m==0: return 0
#     h=[f(s-3,m-1),f(s-5,m-1),f(ceil(s/2),m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19,[s for s in range(24,1000) if f(s,2)])
# print(20,[s for s in range(24,1000) if not f(s,1) and f(s,3)])
# print(21,[s for s in range(24,1000) if not f(s,2) and f(s,4)])