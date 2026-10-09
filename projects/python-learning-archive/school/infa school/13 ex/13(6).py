from ipaddress import*
net= ip_network('136.36.240.16/255.255.255.248',0)
k=0
for ip in net:
    ip2=bin(int(ip))[2:].zfill(32)
    if ip2.count('101') == 0:
        k=k+1
print(k)