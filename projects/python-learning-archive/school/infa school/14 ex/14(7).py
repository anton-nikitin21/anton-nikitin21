for x in range(1,2736):
    x=5**2025+5**1500
    ans=''
    while x != 0:
        ans = str(a%5)+ans
        a=a//5
    if x.count('0') == 527:
        print(x)