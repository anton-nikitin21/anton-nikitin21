for x in range(0,14):
    for y in range (0,16):
        a=1*15**4+2*15**3+3*15**2+x*15+5
        b=6*17**3+7*17**2+y*17+9
        if (a+b)%131 == 0:
            print(x,y, (a+b)//131)
        