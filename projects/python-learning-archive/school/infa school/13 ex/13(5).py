from ipaddress import *
num=0
net= ip_network('192.168.156.235/255.255.255.240',0)
for ip in net:
    
    if ip==ip_address('192.168.156.235'):
        print(num)
    num+=1