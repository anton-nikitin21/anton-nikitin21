# from ipaddress import*

# net = ip_network('135.12.171.214/255.255.248.0',0)
# print(net){}


# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'220.128.112.142/{mask}',0)
#     print(net,net.netmask)


from ipaddress import*
for mask in range(33):
    net=ip_network(f'111.81.208.27/{mask}',0)
    print(net,net.netmask) #показывает маску


# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'148.195.140.28/{mask}',0)
#     print(net)


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'241.185.253.57/{mask}',0)
#     print(net)


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'76.155.48.2/{mask}',0)
#     print(net)

# from ipaddress import*
# for mask in range(33):
#     net1=ip_network(f'157.127.182.76/{mask}',0)
#     net2=ip_network(f'157.127.190.80/{mask}',0)
#     if net1!=net2:
#         print(net1,net2)


# from ipaddress import*
# net=ip_network('0.0.0.0/255.255.254.0')
# print(net.num_addresses-2)#показывает кол-во узлов 


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'108.133.75.91/{mask}',0)
#     print(net,net.num_addresses)


# from ipaddress import*
# for mask in range(33):
#     net = ip_network(f'175.122.80.23/{mask}',0)
#     if net.num_addresses >= 60:
#         print(net)


# from ipaddress import*

# net=ip_network('184.178.54.144/255.255.255.240')
# for ip in net:
#     print(f'{ip:b}')


# from ipaddress import*
# k=0
# net= ip_network('211.48.136.64/255.255.255.224')
# for ip in net:
#     b=f'{ip:b}'
#     if b[-2:]=='11':
#         k+=1
# print(k)


# from ipaddress import*

# net=ip_network('10.8.248.131/255.255.224.0',0)
# print(net)



# from ipaddress import*

# for mask in range (33):
#     net=ip_network(f'118.193.30.139/{mask}',0)
#     print(net,net.netmask)


# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'154.201.208.17/{mask}',0)
#     print(net,net.netmask)

# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'122.21.49.91/{mask}',0)
#     print(net,net.netmask)


# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'173.103.25.118/{mask}',0)
#     print(net)


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'191.173.145.240/{mask}',0)
#     print(net)


# from ipaddress import*
# for mask in range(33):
#     net=ip_network(f'191.173.145.240/{mask}',0)
#     print(net,net.num_addresses)


# from ipaddress import*
# net=ip_network('0.0.0.0/255.255.240.0')
# print(net,net.num_addresses)


# from ipaddress import*

# for mask in range(33):
#     net1=ip_network(f'165.112.200.70/{mask}',0)
#     net2=ip_network(f'165.112.175.80/{mask}',0)
#     if net1==net2:
#         print(net1)\


# from ipaddress import*

# for mask in range(33):
#     net1=ip_network(f'10.96.180.231/{mask}',0)
#     net2=ip_network(f'10.96.140.118/{mask}',0)
#     if net1!=net2:
#         print(net1,net2)



from ipaddress import*
k=0
net=ip_network('192.168.240.0/255.255.255.0')
for ip in net:
    b=bin(int(ip))[2:].zfill(32)
    if b.count('1')==b.count('0'):
        k+=1
print(k)



# from ipaddress import*
# k=0
# net=ip_network('10.48.96.0/255.255.240.0')
# for ip in net:
#     b=bin(int(ip))[2:].zfill(32)
#     if b.count('1')>b.count('0'):
#         k+=1
# print(k)



# from ipaddress import*
# ip = ip_address('238.237.149.255')
# for mask in range(33):
#     net=ip_network(f'238.237.149.255/{mask}',0)
#     if net[0] < ip < net[-1]:
#         print(net,net.broadcast_address)


# from ipaddress import*
# ip1 = ip_address('118.187.59.255')
# ip2 = ip_address('118.187.65.115')
# for mask in range(33):
#     net1 = ip_network(f'118.187.59.255/{mask}',0)
#     net2= ip_network(f'{ip2}/{mask}',0)
#     if net1!=net2:
#         if net1[0]<ip1<net1[-1] and net2[0] < ip2 < net2[-1]:
#             print(net1,net2)



# from ipaddress import*
# k=0
# for A in range(256):
#     ip= ip_address(f'207.0.{A}.167')
#     net= ip_network(f'{ip}/255.255.255.192',0)
#     if all(f'{ip:b}'[:16].count('0')> f'{ip:b}'[16:].count('0') for ip in net):
#         if net[0] < ip < net[-1]:
#             k+=1
# print(k)


from ipaddress import*

k=0

for mask in range(33):
    ip = ip_address('152.65.245.132')
    net= ip_network(f'{ip}/{mask}',0)
    if all(f'{ip:b}'[:16].count('0') >= f'{ip:b}'[16:].count('0') for ip in net):
        print(mask,net.netmask)