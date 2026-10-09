import random 
def f(x):
    return 0.3*x**2-6*x+17 #определяем подынтегральную фунцию



n=100000 #случайные точки
a,b=2,4 #границы интеграла

fmax=max(f(2),f(4)) #нахожу максимум функции на отрезке, то есть верхняя граница области

k=0
for i in range(n):
    x=random.uniform(a,b)
    y=random.uniform(0,fmax) #нахожу рандомные x и y в диапозоне
    if y <= f(x):
        k +=1

area = (k/n)*(b-a)*fmax
print(f'Интеграл: {area:.3f}')
