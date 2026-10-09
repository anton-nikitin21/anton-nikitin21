from ipaddress import*
k=0
net=ip_network('200.33.100.0/255.255.248.0',0)
for ip in net:
    ip2= bin(int(ip))[2:].zfill(32)
    if ip2.count('1')%7!=0:
        k+=1
print(k)