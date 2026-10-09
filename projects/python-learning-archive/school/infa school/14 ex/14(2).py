n=4**644+4**322+16**35-64**3
#count1=0
while n!=0:
    if n%4==0:
          #count+=1
        n =n//4

n=str(n)

print(n.count('3') )