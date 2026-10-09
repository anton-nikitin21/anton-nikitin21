from functools import reduce
a = [1, 4, 7, 2]
result = reduce(lambda x, y: x*y, a)
print(result)
# задание 1 - тест 7

from functools import partial
def func(b, c, a):
    return a*3 + b*2 + c

new_func = partial(func, 7, 6)
a = int(input("Введите а:"))
print(new_func(a), func(7, 6, a))
# задание 2 - тест 7

from functools import cmp_to_key
lst = [45, 78, 813, 56, 126]
def compare(x, y):
    return x - y
sorted_lst = sorted(lst, key=cmp_to_key(compare))
print(sorted_lst[0], sorted_lst[-1])
# задание 3 - тест 7

class distance():
    def __init__(self, meter, santimeter):
        self.meter = meter
        self.santimeter = santimeter
    def __add__(self, other):
        total_santimeters = (self.meter + other.meter)*100 + self.santimeter + other.santimeter
        r_meters = total_santimeters//100
        r_santimeters = total_santimeters%100
        return distance(r_meters, r_santimeters)
    def __str__(self):
        return f'meter: {self.meter} santimeter: {self.santimeter}'

d1=distance(3,67)
d2=distance(4,87)
print("d1 = {}".format(d1))
print("d2 = {}".format(d2))
d3=d1+d2
print("d3 = {}".format(d3))
# задание 4 - тест 7

from functools import total_ordering
@total_ordering
class distance_new(distance):
    def __le__(self, other):
        return (self.meter*100 + self.santimeter) <= (other.meter*100 + other.santimeter)

d1=distance_new(1,20)
d2=distance_new(1,22)
print(d1 <= d2)
print(d1 >= d2)
print(d1 == d2)
print(d2 == d2)
print(d1 < d2)
print(d1 != d2)
# задание 5 - тест 7

class Class():
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    def __invert__(self):
        self.value = str(self.value)[::-2]
        return self

invrt1 = Class('Hello, George')
invrt2 = Class(1.234567)
invertedValue1 = ~invrt1
invertedValue2 = ~invrt2
print(invertedValue1)
print(invertedValue2)
# задание 6 - тест 7

class Person():
    obj_count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.obj_count += 1
        print(f'Создан экземпляр №{Person.obj_count}')
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else: return False
    @classmethod
    def total_objects(cls):
        print(f'Total objects: {cls.obj_count}')

p1 = Person('Иван', 16)
p2 = Person('Дима', 25)
p3 = Person('Анна', 43)
print(Person.is_adult(p1.age))
print(Person.is_adult(p2.age))
Person.total_objects()
# задание 7 - тест 7

from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Number:
    x: int
    y: str

a = Number(2, '123')
b = Number(3, '223')
print(a == b, a < b, a > b)
# задание 8 - тест 7