print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F=((z<=x) and (x<=w)) or (y == (z or x))
                if not F:
                    print(x,y,z,w,F)