# for n in range(1,100):
#     b=bin(n)[2:]
#     if int(b)%2==0:
#         b='10'+b
#     else:
#         b='1' + b + '01'
#     r=int(b,2)
#     if r>516:
#         print(n,r)


# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%3)+s
#         x=x//3
#     return s

# for n in range(10**6,10**7):
#     b=cc(n)
#     b=b.replace('0','4')
#     b=b.replace('2','0')
#     b=b.replace('4','2')
#     z=int(b,3)
#     r=abs(n-z)
#     if r==1_864_246:
#         print(n)
    

# def cc(x):
#     s=''
#     while x>=0:
#         s=str(x%3)+s
#         x=x//3
#     if s =='':
#         s='0'
#     return s
    
# for n in range(1,250):
# n=5
# b=cc(n)
# print(b)
# a=b+ cc(b.count('2'))
# print(a)
# c=a+ cc(a.count('1'))
# print(c)
# z=c+ cc(c.count('0'))
# print(z)
# r=int(z,3)
#     # if r <1000:
# print(n,r)
    
    
    
def cc(x):
    s=''
    while x>0:
        s=str(x%3)+s
        x=x//3
    return s

for n in range(1,450):
    b=cc(n)
    if sum(map(int,b))%3==0:
        b='112' + b[2:]
    else:
        b=b+cc(sum(map(int,b)))
    r=int(b,3)
    if r<=679 and r%2==0:
        print(n,r)
        

