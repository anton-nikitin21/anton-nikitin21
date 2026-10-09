from ipaddress import *

for mask in range(33):
    net = ip_network(f"244.55.138.100/{mask}", 0)
    if net.network_address == ip_address("240.0.0.0"):
        print(net.netmask)