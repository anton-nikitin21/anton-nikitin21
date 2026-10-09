# def f(a,b,d):
#     if a==b and len(d - {2} - {400})>50:
#         return 1
#     if a>b or (a==b and len(d - {2} - {400})<=50):
#         return 0 
#     if a<b:
#         return f(a + 2,b,d|{a+2}) + f(a * 3,b,d|{a*3}) + f(a * 4,b,d|{a*4})
# print(f(2,400,set()))



k=0
from ipaddress import*
net=ip_network('98.81.154.195/255.252.0.0',0)
for ip in net.hosts():
    k+=1
print(k)