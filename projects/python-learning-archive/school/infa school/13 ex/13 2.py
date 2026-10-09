# from ipaddress import*

# for mask in range(33):
#     net=ip_network(f'238.237.149.255/{mask}',0)
#     print(net,net.broadcast_address)



# from ipaddress import*
# k=0
# net=ip_network('98.81.154.195/255.252.0.0',0)
# for ip in reversed(str(net)):
#     print(ip)


from ipaddress import*
k=0
net=ip_network('123.222.111.192/255.255.255.192')
for ip in net:
    c=bin(int(ip))[2:].zfill(32)
    if ((c[8:16]).count('0')+(c[24:]).count('0'))%5!=0:
        k+=1
print(k)