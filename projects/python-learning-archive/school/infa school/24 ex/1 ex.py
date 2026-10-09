# s = open('24_3.txt').readline()
# s = s.replace('Y', 'X').replace('Z', 'X')
# while 'XX' in s:
#     s = s.replace('XX', 'X X')
# print(s[:100])
# s = s.split()
# print(s[:4])

# m = 0
# for i in s:
#     m = max(m, len(i))
# print(m)




s = open('24_21421.txt').readline().rstrip()

a = set(s)

for i in a:
    if i not in '0123456789AB':
        s = s.replace(i, ' ')
s = s.split()

m = 0
for i in s:
    i = i.lstrip('0')
    for j in '13579B':
        if j in i:
            i = i.rstrip(j)
    m = max(m, len(i))

print(m)