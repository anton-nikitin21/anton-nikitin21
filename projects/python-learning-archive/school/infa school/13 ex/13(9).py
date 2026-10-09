from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'120.91.85.213/{mask}',0)
    ip1= ip.adress('120.91.89.205')
    net2 = ip_network(f'120.91.89.205/{mask}',0)
    ip2= ip.adress('120.91.85.213')
    if ip1 not in net1 or ip2 not in net2:
        print(net1.netmask,net2.netmask)