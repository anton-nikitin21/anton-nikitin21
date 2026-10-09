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
