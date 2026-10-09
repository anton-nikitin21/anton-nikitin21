from ipaddress import*
k=0
net=ip_network('172.16.168.0/255.255.248.0',0)
for ip in net:
    ip2= bin(int(ip))[2:].zfill(32)
    if ip2.count('1')%5!=0:
        k+=1
print(k)