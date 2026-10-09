from ipaddress import *

for mask1 in range(33):
    net1 = ip_network(f"10.96.180.231/{mask1}", 0)
    print(net1.netmask)
print("      ")
for mask2 in range(33):
    net2 = ip_network(f"10.96.140.118/{mask2}", 0)
    
    print(net2.netmask)
    
        