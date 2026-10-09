def cc(x):
    s=''
    d='0123456789abcdefghi'
    while x>0:
        s=d[x%19] + s
        x=x//19
    return s

# for x in range(1,1000):
#     a=9*19**7+8*19**6+8*19**5+9*19**4+7*19**3+x*19**2+2*19+1
#     b=2*19**4+x*19**3+9*19**2+2*19+3
#     c=a + b
#     if c%18==0:
#         print(x)


    