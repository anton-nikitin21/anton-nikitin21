from ipaddress import *
k=0
net=ip_network('228.172.236.0/255.255.240.0',0) 
for ip in net:
    ip2 = bin (int(ip))[2:].zfill(32)
    if ip2.count('1')%5!=0:
        k+=1
print(k)