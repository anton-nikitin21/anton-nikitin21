print('a b c F')
for a in 0,1:
    for b in 0,1:
        for c in range(2):
                F=(not a) or (not b) and c 
                if not F:
                    print(a,b,c,F)