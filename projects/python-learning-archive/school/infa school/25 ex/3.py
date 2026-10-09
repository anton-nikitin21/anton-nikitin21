# k=0
# for i in range(800_001,10**6+1):
#     d=set()
#     for j in range(2,int(i**0.5)+1):
#         if i%j == 0:
#             d.add(j)
#             d.add(i//j)
#     if len(d)>0:
#         M=min(d)+max(d)
#         if M%10 == 4:
#             print(i,M)
#             k+=1
#             if k==5:
#                 break



# k=0
# for i in range(174457,174506):
#     d=set()
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             d.add(j)
#             d.add(i//j)
#     d=sorted(d)
#     if len(d)==2:
#         print(d[0],d[1])



# k=0
# for i in range(81234,134690):
#     d=set()
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             d.add(j)
#             d.add(i//j)
            
#     d=sorted(d)
#     if len(d)==3:
#         print(d[0],d[1],d[2])



# k=0
# for i in range(150001,10**10):
#     d=set()
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             d.add(j)
#             d.add(i//j)
            
#     if len(d)>0:
#         S=sum(d)
#     else:
#         S=0
#     if S%13==10:
#         print(i,S)
#         k+=1
#         if k==7:
#             break


# for i in range(190201,190261):
#     d=set()
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             d.add(j)
#             d.add(i//j)
            
#     if len(d)==4:
#         print(i,d)
            
            
# k=0           
# for i in range(500001,10**10):
#     d=set()
#     for j in range(1,int(i**0.5)+1):
#         if i%j==0:
#             d.add(j)
#             d.add(i//j)
            
#     if len(d)>0:
#         R=sum(d)
#         if R%10==6:
#             print(i,R)
#             k+=1
#             if k==5:
#                 break



# k=0

# for i in range(345679,10**10):
#     d=set()
#     for j in range(1,int(i**0.5)+1):
#         if i%j==0:
#             d.add(j)
#             d.add(i//j)
    
#     if len(d)>0:
#         a=[x for x in d if x%2!=0]
#         F=int(sum(a)/len(a))
#         if F!=0 and F%37==0:
#             print(i,F)
#             k+=1
#             if k==5:
#                 break


# from fnmatch import*
# for i in range(84318,10**12,84318):
#     if fnmatch(str(i),'5*7?'):
#         a=[int(x) for x in str(i) if str(i).count(x)==1]
#         if len(a)==len(str(i)):
#             print(i,i//84318)