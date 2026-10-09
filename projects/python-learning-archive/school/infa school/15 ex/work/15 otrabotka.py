# for A in range(1,1000):
#     ok=True
#     for x in range(1,1000):
#         F=(((x&13!=0) or (x&A!=0))<=(x&13!=0)) or ((x&A!=0) and (x&39==0))
#         if not F:
#             ok=False
#             break
#     if ok:
#         print(A)

# def dell(n,m):
#     return n%m==0

# for A in range(1,1000):
#     OK=True
#     for x in range(1,1000):
#         F=((dell(x,15) and (not dell(x,21))) <= (not(dell(x,A)) or (not(dell(x,15)))))
#         if not F:
#             OK=False
#     if OK:
#         print(A)
#         break
    
# for A in range(1,1000):
#     ok=True 
#     for x in range(1,1000):
#         for y in range(1,1000):
#             F=(2*x+y!=70) or (x<y) or (A<x)
#             if not F:
#                 ok =False
#                 break
#     if ok:
#         print(A)
#         break

# def f(x,y,a):
#     return (x*y>a) and (x>y) and (x<8)

# for a in range(1,1000):
#     if all(f(x,y,a)==0 for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break


# def f(x,y,a):
#     return (2*x+y!=70) or (x<y) or (a<x)

# for a in range(1,300):
#     if all(f(x,y,a)==1 for x in range(300) for y in range(300)):
#         print(a)

# def f(x,y,A):
#     return (x>39) or (y>26) or ((2*x + 4*y) <A)

# for A in range(1,1000):
#     if all(f(x,y,A)==1 for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break


# a=1
# c=[]
# for x in range(70):
#     p=x in {2,4,6,8,10,12,14,16,18,20}
#     q=x in [5,10,15,20,25,30,35,40,45,50]
#     f = (a <= p) and (q <= (not(a)))
#     if f:
#         c.append(x)
# print(len(c))


# a=[]
# for x in range(1,70):
#     p=x in {2,4,6,8,10,12,14,16,18,20}
#     q=x in [5,10,15,20,25,30,35,40,45,50]
#     f = ((x in a) <= p) and (q <= (not(x in a)))
#     if f:
#         a.append(x)
# print(len(a))


# a=1
# c=[]
# for x in range(1,1000):
#     d=x in {s for s in range(17,59)}
#     c=x in {i for i in range(29,81)}
#     f= d <= (((not(c)) and (not(a))) <= (not(d)))
#     if f:
#         c.append(x)
# print(len(c))



# def dell(m,n):
#     if m%n==0: 
#         return 1
#     else: 
#         return 0
# k=0   
# def f(x,a):
#     return dell(a,25) and ((dell(x,24) and dell(x,75)) <= dell(x,a))
# for a in range(-1000,1000):
#     if a !=0:
#         if all(f(x,a)==1 for x in range(-1000,1000)):
#             k+=1
# print(k)



# def f(x,a):
#     return ((x&17!=0) <= ((x&a!=0) <=(x&58!=0))) <= ((x&8==0) and (x&a!=0) and (x&58==0))
# for a in range(43,56):
#     if all(f(x,a)==0 for x in range(1,1000)):
#         print(a)



# def pl(a,b,c):
#     return a*b > c

# def f(x,y,a):
#     return (not(pl(x,y,a+13))) <= (pl(28,y,520) or pl(x,25,800))

# d=[]
# for a in range(-500,1000):
#     if all(f(x,y,a)==1 for x in range(1,1000) for y in range(1,1000)):        
#         d.append(a)
# print(max(d))

from itertools import*

# def f(x):
#     p = x in {2,4,6,8,10,12,14,16,18,20}
#     q = x in {5,10,15,20,25,30,35,40,45,50}
#     a = a1 <= x <= a2
#     return (a <= p) and (q <= (not(a)))

# ox = [x/4 for x in range(1*4,60*4)]
# d=[]

# for a1, a2 in combinations(ox,2):
#     if all(f(x) ==1 for x in ox):
#         d.append((a2-a1,a1,a2))
# print(d) 




# def dell(x,A):
#     if x%A==0:
#         return True
#     else: return False
    
# def f(x,A):
#     return ((not(dell(x,84))) or (not(dell(x,90)))) <= (not(dell(x,A)))

# for A in range(1,2000):
#     if all(f(x,A)==1 for x in range(1,3000)):
#         print(A)




# def f(x,a):
#     return ((x&26!=0) or (x&13!=0)) <= ((x&29==0) <= (x&a!=0))

# for a in range(1,1000):
#     if all(f(x,a)==1 for x in range(1,3000)):
#         print(a)



# def f(x,a):
#     return (x&107==0) <= ((x&55!=0) <= (x&a!=0))

# for a in range(1,1000):
#     if all(f(x,a)==1 for x in range(1,3000)):
#         print(a)





# from math import*
# def f(x,y,a):
#     return (x**2 -10*x+16>0) or (y**2-10*y+21>0) or (x*y< 2*a)

# for a in range(0,1000):
#     if all(f(x,y,a)==1 for x in range(1,3000) for y in range(1,3000)):
#         print(a)



1,3,5,7,9,11,13,15,17,19
2,