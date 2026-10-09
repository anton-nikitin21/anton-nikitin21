for x in range(0,50):
    for y in range(0,50):
        for z in range(0,50):
            s= '0' + x * '1' + y * '2' + z*'3'
            while '00' not in s:
                s=s.replace ('01','21022',1)
                s=s.replace ('02','310',1)
                s=s.replace ('02','230112',1)
            if s.count('1') == 96 and s.count('2') == 36 and s.count('3') == 80:
                print(x+z+y+2)