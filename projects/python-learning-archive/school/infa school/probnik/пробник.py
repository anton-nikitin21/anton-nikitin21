# print('w,x,y,x,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=(x<=y) and not(w) and z
#                 if F:
#                     print(w,x,y,z,F)


# for n in range(1,100):
#     b=bin(n)[2:]
#     if sum(map(int,b))%2==0:
#         b=b+'11'
#     else:
#         b=b+'01'
#     r=int(b,2)
#     if r>61:
#         print(n,r)


# from turtle import*
# tracer(0)
# screensize(5000,5000)
# r=15

# for i in range(5):
#     fd(8*r)
#     rt(90)
#     fd(11*r)
#     rt(90)
    
# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(4,'red')
        
# update()
# mainloop()

# i=51
# M=16*1000
# t=26*60
# V=M*i*t*2
# print(V//2**26)

# from math import*
# k=256
# i=ceil(log2(10+4080))
# I=ceil(k*i/8)
# z=I*2**16
# print(z/1024/1024)


# s=68*'9'
# while '22222' in s or '9999' in s:
#     if '22222' in s:
#         s=s.replace('22222','99',1)
#     else:
#         s=s.replace('9999','29',1)
# print(s)


# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%4)+s
#         x=x//4
#     return s

# a=4**644+4**322+16**35-64**3
# b=cc(a)
# print(b.count('3'))

# def f(x,y,a):
#     return (x<=19) or (y<2*x+a-50) or (y>17)

# for a in range(1,300):
#     if all(f(x,y,a)==1 for x in range(1,300) for y in range(1,300)):
#         print(a)
#         break


# def f(n):
#     if n>400:
#         return n**n
#     if n<=400:
#         return n+6+f(n+12)
# print(f(72)-f(108))


# f=open('')
# a=[int(s) for s in f]

# k=[]
# for i in range(1,len(a)-1):
#     if abs(a[i])%77+abs(a[i+1])%77==min(a):
#         k.append(abs(a[i])%77+abs(a[i+1])%77)
# print(len(k),max(k))


# def f(s,m):
#     if s>=54: return m%2==0
#     if m==0:return 0
#     h=[f(s+2,m-1),f(s*2,m-1)]
#     return any(h) if  (m-1)%2==0 else all(h)

# print(19,[s for s in range(1,54) if f(s,2)])
# print(20,[s for s in range(1,54) if not f(s,1) and f(s,3)])
# print(21,[s for s in range(1,54) if not f(s,2) and f(s,4)])      



# import sys
# sys.setrecursionlimit(3000)

# def F(n):
#     s=0
#     if n<3:
#         return 1
#     if n>2 and n%2!=0:
#         return F(n-1)-F(n-2)
#     if n>2 and n%2==0:
#         for i in range(1,n-1+1):
#             s=s+F(i)
#         return s
    
# print(F(39))


# f=open('.txt')
# a=[int(i) for i  in f]
# k=[]
# for i in range(0,len(a)-1):
#     if (abs(a[i]))%10==5 and (abs(a[i+1]))%10==5:
#         k.append(abs(a[i]-a[i+1]))
        
# print(len(k),max(k))

# def f(a,b,m):
#     if a+b>=101: return m%2==0
#     if m==0:return 0
#     h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)


# print(19,[s for s in range(1,94) if f(7,s,2)])
# print(20,[b for b in range(1,94) if not f(7,b,1) and f(7,b,3)])
# print(21,[b for b in range(1,94) if not f(7,b,2) and f(7,b,4)])



# def f(start,end):
#     if start == end:
#         return 1
#     if start < end:
#         return 0
#     if start > end:
#         return f(start -8,end) + f(start//2 ,end)
# print(f(102,43)*f(43,5))

# def f(start,end):
#     if start==end:
#         return 1
#     if start> end:
#         return 0
#     if start < end:
#         return f(start + 2,end) + f(start*2,end) + f(start*3,end)
# print(f(1,6)*f(6,24))



# from turtle import*

# tracer(0)
# screensize(5000,5000)
# r=70
# lt(90)
# rt(60)
# for i in range(4):
#     fd(8*r)
#     rt(120)
#     fd(4*r)
#     rt(240)
    
# rt(120)
# fd(2*r)
# rt(90)
# fd(r*(16*(3**(1/2))))
# rt(90)
# fd(2*r)

# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(4,'red')
        
# update()
# mainloop()




# from fnmatch import*
# for i in range(4321,10**9+1,4321):
#     if fnmatch(str(i), '34*56?7'):
#         k=1
#         s=str(i)
#         for j in s:
#            k=int(j)*k
#         if k%10==0:
#             print(i,k)
            


# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%3)+s
#         x=x//3
#     return s
# k=[]
# for n in range(1,1000):
#     b=cc(n)
#     if sum(map(int,b))%3==0:
#         b='112'+b[2:]
#     else:
#         b=b+cc(sum(map(int,b)))
#     r=int(b,3)
#     if r<=679 and r%2==0:
#         k.append(r)
# print(max(k))
    
    
    
# print('x,y,z,w,F')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F=(x and y or (not(x))) and w or z
#                 print(x,y,z,w,F)




# s='2'+140*'3'
# while '2' in s:
#     if '23' in s:
#         s=s.replace('23','3332',1)
#     else:
#         s=s.replace('2','333',1)
        
# print(sum(map(int,s)))


# for x in range(22):
#     a=9*22**7+8*22**6+x*22**5+7*22**4+9*22**3+6*22**2+4*22+1
#     b=2*22**4+5*22**3+x*22**2+4*22+9
#     c=6*22**3+3*22**2+x*22+5
#     v=a+b+c
#     if v%21==0:
#         print(x,v/21)



# import sys
# sys.setrecursionlimit(30000)

# def F(n):
#     if n<=5: 
#         return 1000
#     else:
#         return n + 3 + F(n-2)
    
# print(3*F(53079)-(F(53077)+F(53075)+F(53073)))

# f = open('17.txt')
# a = [int (i) for i in f]
# c = 0
# for i in a:
#     if len(str(abs(i))) == 4 and str(i)[-1] == '3':
#         c += 1
        
# otvet = []
# for i in range(len(a) - 2):
#     k = []
#     k.append(a[i]) 
#     k.append(a[i+1]) 
#     k.append(a[i+2])
#     k.sort()
#     if k[1] + k[2] > c ** 2:
#         otvet.append(a[i] + a[i + 1] + a[i + 2])
        
# print(len(otvet), abs(max(otvet)))




# print('w,x,y,z,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=(w and z or (not(w))) and x or y
#                 if F:
#                     print(w,x,y,z,F)






# k=0    
# for i in range(1125001,10**10+1):
#     d=set()
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             if j%10==7 and j!=7:
#                 d.add(j)
#             if (i//j)%10==7 and (i//j)!=7:    
#                 d.add(i//j)

#     if len(d)>0:
#         k+=1
#         print(i,min(d))
#         if k==5:
#             break


# print('x,y,z,w,F')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F=not(((not(x)) or y) and (not(w))) or (not(z and(not(y and w))))
#                 if not F:
#                     print(x,y,z,w,F)




# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%3)+s
#         x=x//3
#     return s

# for n in range(1,250):
#     b=cc(n)
#     if n %3 ==0:
#         b=b +b[-2:]
#     else:
#         b=b+cc(int(sum(map(int,b))))
#     r=int(b,3)
#     if r>220 and r%2==0:
#         print(n,r)



# from turtle import*
# tracer(0)
# screensize(5000,5000)
# r=15
# lt(90)

# for i in range(8):
#     fd(16*r)
#     rt(90)
#     fd(22*r)
#     rt(90)
# up()
# fd(5*r)
# rt(90)
# fd(5*r)
# lt(90)
# down()
# for i in range(8):
#     fd(52*r)
#     rt(90)
#     fd(77*r)
#     rt(90)
    
# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(4,'red')

# update()
# mainloop()


# from math import*
# i=ceil(log2(2**24))
# k=3840*2160
# I=int(i*k/8/1024)
# print(I)



# for x in range(1,21):
#     a=x*4**21+5*3**21+B+x+8\
    
    
    
    
# def f(s,m):
#     if s<=24: return m%2==0
#     if m==0: return 0
#     h=[f(s-3,m-1)]
#     if s%2==0:
#         h.append(f(s//2,m-1))
#     else:
#         h.append(f((s+3)//2,m-1))
#     return any(h) if (m-1)%2==0 else all(h)

# print(19, [s for s in range(25,200) if f(s,2)])
# print(20, [s for s in range(25,200) if not f(s,1) and f(s,3)])
# print(21, [s for s in range(25,200) if not f(s,2) and f(s,4)])
    
    




# print('w,x,y,z,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=(x and (not(y))) or (y==z) or w
#                 if not F:
#                     print(w,x,y,z,F)





# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%2)+s
#         x=x//2
#     return s

# for n in range(1,250):
#     b=cc(n)
#     b=b+str(sum(map(int,b))%2)
#     b=b+str(sum(map(int,b))%2)
#     r=int(b,2)
#     if r>253:
#         print(n,r)
    
    
    
    
# from turtle import*

# screensize(5000,5000)
# tracer(0)
# r=15
# rt(90)
# for i in range(7):
#     rt(45)
#     fd(11*r)
#     rt(45)
    
# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(4,'red')
        
# update()
# mainloop() 


# from math import*
# i1=ceil(log2(2**23))
# k1=1024*768
# I1=(i1*k1/8/1024)
# print(I1)
# i2=ceil(log2(2**22))
# k2=800*600
# I2=(i2*k2/8/1024)
# print(I2)
# print(100*(I1-I2))





# from math import*
# for i in range(1,250):
#     I=ceil(246*i/8)
#     if 703569*I <=77*1024*1024:
#         print(I,i,2**i)




# for n in range(3,10**4):
#     s='1'+'9'*n
#     while '19' in s or '399' in s or '999' in s:
#         if '19' in s:
#             s=s.replace('19','9',1)
#         if '399' in s:
#             s=s.replace('399','91',1)
#         if '999' in s:
#             s=s.replace('999','3',1)
#     if sum(map(int,s))==33:
#         print(n)     




# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%7)+s
#         x=x//7
#     return s
# for x in range(1,2301):
#     z=7**350+7**150-x
#     b=cc(z)
#     if b.count('0')==200:
#         print(x)


# def f(x,A):
#     return (((x&52)!=0) and ((x&48)==0)) <= (not (x&A==0))

# for A in range(1,2000):
#     if all(f(x,A)==1 for x in range(1,2000)):
#         print(A)
#         break


# from sys import*
# setrecursionlimit(30000)
# def F(n):
#     if n>=2025:
#         return n
#     if n<2025:
#         return 2*n + F(n+2)
# print(F(82)-F(81))




# def f(s,m):
#     if s>=67:return m%2==0
#     if m == 0:return 0
#     h=[f(s+1,m-1),f(s+4,m-1),f(s*3,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19, [s for s in range(1,67) if f(s,2)])
# print(20, [s for s in range(1,67) if not f(s,1) and f(s,3)])
# print(21, [s for s in range(1,67) if not f(s,2) and f(s,4)])




# from turtle import*
# screensize(10000)
# tracer(0)
# r=15
# color('red')
# lt(90)
# #я
# fd(10*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(225)
# fd(7*r)

# lt(135)
# up()
# fd(10*r)
# fd(2.5*r)
# lt(90)
# down()
# fd(10*r)
# lt(90)
# fd(3*r)
# rt(180)
# fd(6*r)

# up()
# fd(r)
# down()

# fd(5*r)
# lt(180)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(180)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)

# up()
# fd(r)
# down()

# lt(90)
# fd(10*r)
# rt(90)
# fd(5*r)
# lt(180)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# rt(90)
# fd(5*r)
# rt(90)
# fd(5*r)
# rt(180)
# fd(5*r)

# up()
# fd(r*6)
# down()

# lt(90)
# fd(10*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(225)
# fd(7*r)

# lt(135)
# up()
# fd(10*r)
# down()

# lt(80)
# fd(10.5*r)
# rt(160)
# fd(10.5*r)
# lt(80)

# up()
# fd(r)
# down()
# lt(90)
# fd(10*r)
# rt(180)
# fd(5*r)
# lt(90)
# fd(1.5*r)
# rt(90)
# fd(5*r)
# lt(90)
# fd(3*r)
# lt(90)
# fd(10*r)
# lt(90)
# fd(3*r)
# lt(90)
# fd(5*r)

# up()
# lt(90)
# fd(4*r)
# rt(90)
# fd(5*r)
# lt(90)
# down()
# lt(90)
# fd(10*r)
# rt(90)
# fd(5*r)
# lt(180)
# fd(5*r)
# lt(90)
# fd(5*r)
# lt(90)
# fd(5*r)
# rt(90)
# fd(5*r)
# rt(90)
# fd(5*r)
# rt(180)
# fd(5*r)

# up()
# fd(r)
# down()


# lt(80)
# fd(10.5*r)
# rt(160)
# fd(10.5*r)
# lt(80)

# up()
# fd(r)
# down()
# lt(90)
# fd(10*r)
# rt(180)
# fd(5*r)
# lt(90)
# fd(1.5*r)
# rt(90)
# fd(5*r)
# lt(90)
# fd(3*r)
# lt(90)
# fd(10*r)
# lt(90)
# fd(3*r)
# lt(90)
# fd(5*r)

# update()
# mainloop()





# def f(start,end):
#     if start == end:
#         return 1
#     if start < end:
#         return 0
#     if start > end and end!=0 :
#         return f(start -start,end) + f(start//2 ,end)+f(start-end,end)
#     if start > end and end==0 :
#         return f(start -start,end) + f(start//2 ,end)+f(start-2,end)
# print(f(47,40)*f(40,18)*f(18,14))



# from fnmatch import*
# for  i in range(84318,10**12,84318):
#     if fnmatch(str(i),'5*7?'):
#         a1 =[x for x in str(i) if (str(i)).count(x)==1]
#         if len(a1)==len(str(i)):
#             print(i,i//84318)

      
# from ipaddress import*

# net = ip_network('135.12.171.214/255.255.248.0',0)
# print(net)



# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'220.128.112.142/{mask}',0)
#     print(net,net.netmask)


# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'111.81.208.27/{mask}',0)
#     print(net,net.netmask)


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'148.195.140.28/{mask}',0)
#     print(net,net.netmask) 


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'241.185.253.57/{mask}',0)
#     print(net,net.netmask)



# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'76.155.48.2/{mask}',0)
#     print(net,net.netmask)


# from ipaddress import*
# for mask in range(33):
#     net1=ip_network(f'112.117.107.70/{mask}',0)
#     net2=ip_network(f'112.117.121.80/{mask}',0)
#     if net1==net2:
#         print(net1,net1.netmask)


# from ipaddress import*
# for mask in range(33):
#     net1=ip_network(f'157.127.182.76/{mask}',0)
#     net2=ip_network(f'157.127.190.80/{mask}',0)
#     if net1!=net2:
#         print(net1,net2)


# from ipaddress import*

# net=ip_network('0.0.0.0/255.255.254.0',0)
# print(net.num_addresses-2)


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'175.122.80.13/{mask}',0)
#     print(net, net.num_addresses)




# from ipaddress import*
# k=0
# net=ip_network('184.178.54.144/255.255.255.240')
# for ip in net:
#     # b=f'{ip:b}'
#     b=bin(int(ip))[2:].zfill(32)
#     if '111' in  b:
#         print(b)
#         k+=1
# print(k)




# from ipaddress import*
# k=0
# net=ip_network('211.48.136.64/255.255.255.224',0)
# for ip in net:
#     b=bin(int(ip))[2:].zfill(32)
#     if b[-1]=='1' and b[-2]=='1':
#         print(b)
#         k+=1
        
# print(k)

# from ipaddress import*

# net=ip_network('192.168.156.235/255.255.255.240',0)
# print(net) #192.168.156.224/28

# ip1=ip_address('192.168.156.235')
# ip2=ip_address('192.168.156.224')
# print(int(ip1)-int(ip2))



# from ipaddress import*
# K=0
# net=ip_network('0.0.0.0/255.255.128.0')
# for ip in net:
#     if int(ip)%4==0:
#         K+=1
# print(K)



from ipaddress import*

net=ip_network('98.71.254.171/255.248.0.0',0)
for ip in net:
    c=bin(int(ip))[2:].zfill(32)
    if c.count('1')%7==0:
        print(ip)
        input()
        