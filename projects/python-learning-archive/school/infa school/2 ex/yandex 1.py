print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for w in range(2):
            for z in range(2):
                F=not(y<=(x==w)) and (z<=x)
                if F:
                    print(x,y,z,w,F)