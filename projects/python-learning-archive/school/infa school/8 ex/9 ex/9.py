# f=open('93.txt')
# k=0
# for s in f:
#     a=sorted([int(x) for x in s.split()])
#     if a[3]<a[0]+a[1]+a[2]:
#         if a[0]+a[3] == a[2]+a[1] or a[0]+a[2]==a[1]+a[3]:
#             k+=1
# print(k)





# f=open('95.txt')
# for s in f:
#     a=sorted({int(x) for x in s.split()})
#     if 





# print('w,x,y,z,F')
# for w in 0,1:
#     for x in 0,1:
#         for y in 0,1:
#             for z in 0,1:
#                 F=((z<=x) and (x<=y)) or (w==(z or x))
#                 if not F:
#                     print(w,x,y,z,F)
    
    
# def cc(x):
#     s=''
#     while x>0:
#         s=str(x%2)+s
#         x=x//2
#     return s

# for n in range(1,150):
#     b=cc(n)
#     if sum(map(int,b))%2==0:
#         b='11' + b[2:] +'1'
#     else:
#         if b.count('0')<b.count('1'):
#             b=b+'0'
#         else:
#             b=b+'1'
#     r=int(b,2)
#     if r>271:
#         print(n,r)



# from turtle import*
# screensize(5000)
# tracer(0)
# left(90)
# r=15
# rt(30)
# for i in range(18):
#     fd(11*r)
#     rt(120)
#     fd(11*r)
#     rt(60)
    
# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r,y*r)
#         dot(4,'red')
        
# update()
# mainloop()

# for i in range(1,1000):
#     v=2*96*1000*(3*60+33)*i
#     if 0.6*v <= 25*1024*1024*8:
#         print(i)


from itertools import*
k=0
z=0
for x in product(sorted('ЦИФЕРБЛАТ'),repeat=5):
    s=''.join(x)
    k+=1
    if k%2!=0:
        if s[0] not in 'ИЕА':
            if s.count('Ц')==s.count('Ф'):
                z+=1
print(z)
                
    
    