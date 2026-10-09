print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                F=((not z) == (not y)) or (not x and not y) or w 
                if not F:
                    print(x,y,z,w,F)