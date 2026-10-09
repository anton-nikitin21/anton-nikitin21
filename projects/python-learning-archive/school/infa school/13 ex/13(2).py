from ipaddress import *

for mask in range(33):
    net = ip_network(f"244.55.229.28/{mask}", 0)
    if net.network_address == ip_address("244.0.0.0"):
        print(32 - mask)