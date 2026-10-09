print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F=(not(z)) and x or x and y
            print(x,y,z,F)  