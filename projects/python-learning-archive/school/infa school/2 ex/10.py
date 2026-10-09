print('w x y z F')
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                F= ((w <= y) <= x) or not(z)
                if not F:
                    print(w,x,y,z,F)