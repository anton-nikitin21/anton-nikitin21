from ipaddress import *

for x in range(256):
    try:
        net=ip_network(f'172.16.168.0/255.255.255.{x}',0)
        k=0
        for ip in net:
            ip2=bin(int(ip))[2:].zfill(32)
            if ip2.count('0')%7==0:
                k+=1
        if k==35:
            print(x)
    except:
        ...
    