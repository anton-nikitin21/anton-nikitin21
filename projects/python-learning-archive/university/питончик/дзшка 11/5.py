from itertools import chain
iteratir = chain([1,2], ['a','b','c'], [3,4,5,6])
print(f'Type of the new iterator: {type(iteratir)}')
print(f'Elements of the new iterator:', *[x for x in iteratir])
# задание 1 - тест 5

from itertools import permutations
iteratir = permutations("Pyt", 2)
print(*[x for x in iteratir])
# задание 2 - тест 5

from itertools import zip_longest, chain
iteratir = zip_longest([100, 200, 300, 400], [10, 20, 30, 40], [1, 2, 3, 4])
result_it = chain.from_iterable(iteratir)
print([x for x in result_it])
# задание 3 - тест 5

def generator(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a**2

print(*generator(12))
# задание 4 - тест 5

def generator(n):
    c = 1
    for k in range(n+1):
        yield c
        c = c * (n-k+1) // (k+1)

print(*generator(7))
# задание 5 - тест 5

from itertools import product
def generator(n, k):
    result_iter = product(range(k), repeat=n)
    for x in result_iter:
        yield f'{x[0]} {x[1]}'

print(*generator(2, 3), sep='\n')
# задание 6 - тест 5

class Class():
    def __init__(self, parametr):
        self.__parametr = parametr
    @property
    def parametr(self):
        return self.__parametr
    @parametr.setter
    def parametr(self, value):
        self.__parametr = value

obj = Class(1)
print(obj.parametr)
obj.parametr = 2
print(obj.parametr)
# задание 7 - тест 5

class Class():
    __class_parametr = 10
    @property
    def parametr(self):
        return Class.__class_parametr
    @parametr.setter
    def parametr(self, value):
        if value % 2 == 0:
            Class.__class_parametr = 2
        else:
            Class.__class_parametr = 1

obj = Class()
print(obj.parametr)
obj.parametr = 10
print(obj.parametr)
obj.parametr = 11
print(obj.parametr)
# задание 8 - тест 5