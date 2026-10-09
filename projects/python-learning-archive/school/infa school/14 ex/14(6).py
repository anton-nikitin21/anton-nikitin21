for x in range(1,2031):
    a=3**100-x
    d= []
    while a > 0:
        d = [a%3] + d
        a = a//3
    if d.count(0) == 5:
        print(x)

        