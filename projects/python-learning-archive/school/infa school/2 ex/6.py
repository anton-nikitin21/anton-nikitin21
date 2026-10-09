print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F= ((x and not y) or (w<=z)) == (z==x)
                if F:
                    print(x,y,z,w)