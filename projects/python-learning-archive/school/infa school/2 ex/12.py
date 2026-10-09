print('w,x,y,z,F')
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
               F=(not(x <= z) or (y==w) or y)
               if not F:
                    print(w,x,y,z,F)