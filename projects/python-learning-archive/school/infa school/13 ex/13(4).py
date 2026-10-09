from ipaddress import*
a=0
for mask in range(33):
    net= ip_network(f'76.155.48.2/{mask}',0)
    if net.network_address == ip_address('76.155.48.0'):
        a+=1
print(a)