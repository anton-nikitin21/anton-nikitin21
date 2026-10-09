n=3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2025
count=0
while n!=0:
    if n%25==0:
          count+=1
    n=n//25
print(count)