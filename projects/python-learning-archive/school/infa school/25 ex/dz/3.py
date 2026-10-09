""" from fnmatch import* """
""" k=0 """
""" for i in range(65001,10**5,1): """
"""     d=set() """
"""     for j in range(2,int(i**0.5)+1): """
"""         if fnmatch(str(i),'6*97*5'): """
"""             if i%j == 0 and j%2==0: """
"""                 d.add(j) """
"""                 print(i) """
"""                 k+=1 """
"""                 if k==7: """
"""                     break """
                
            
