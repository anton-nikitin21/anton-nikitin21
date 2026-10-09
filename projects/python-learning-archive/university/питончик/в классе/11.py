import math
import mpmath 

mpmath.mp.dps = 50  # кол-во знаков после запятой

x = mpmath.mpf(20)  # наш x с высокой точностью


#считаем 
exp = mpmath.exp(4*x + 5)

#косинус от exp
cos = mpmath.cos(exp)

#корень из трех
z3 = mpmath.root(x, 3)

y = cos * z3

print("Результат вычисления:", y)

# with open("req.txt", "w") as f:
#     import mpmath
#     f.write(f"mpmath=={mpmath.__version__}/n")
    
