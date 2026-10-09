from logging import *
basicConfig(level=INFO)
def logging(func):
    def wrapper(*args):
        result = func(*args)
        info(f'Сработала функция: {func.__name__} и вернула: {result}')
        return result
    return wrapper

@logging
def cube(n):
    return n**3

print(cube(3))
# задание 1 - тест 8

class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age= age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value
    @age.deleter
    def age(self):
        del self.__age

p = Person('Сергей', 20)
print(p.__dict__)
print(p.age)
p.age = 35
print(p.age)
del p.age
print(p.__dict__)
p.age = 10
print(p.age)
# задание 2 - тест 8

class Vector():
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def if_v_otrezke(cls, n):
        return cls.MIN_COORD <= n <= cls.MAX_COORD
    @staticmethod
    def r_len(x, y):
        return (x**2 + y**2)**0.5
    def __init__(self, x, y):
        if self.if_v_otrezke(x) and self.if_v_otrezke(y):
            self.x = x
            self.y = y
            print(self.r_len(x, y))
        else:
            self.x = 0
            self.y = 0
            print(self.r_len(0, 0))
    def get_coord(self):
        return (self.x, self.y)

v = Vector(10, 20)
print(v.get_coord())
w = Vector(10, 200)
print(w.get_coord())
# задание 3 - тест 8

from functools import singledispatch

@singledispatch
def func(arg):
    raise NotImplementedError("Неподдерживаемый тип")
@func.register
def _(arg: int):
    return arg ** 3
@func.register
def _(arg: str):
    return arg.upper()
@func.register
def _(arg: list):
    return arg * 2

print(func(2))
print(func('Python'))
print(func([1, 2, 3]))
print(func({1: 2, 2: 3}))
# задание 4 - тест 8

import math
class Complex:
    def __init__(self, a, b):
        self.a = a  #действительная часть
        self.b = b  #мнимая часть
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        # (a+bi)*(c+di) = (ac-bd) + (ad+bc)i
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return Complex(real, imag)
    def __truediv__(self, other):
        # (a+bi)/(c+di) = [(ac+bd) + (bc-ad)i] / (c^2 + d^2)
        denom = other.a**2 + other.b**2
        real = (self.a * other.a + self.b * other.b) / denom
        imag = (self.b * other.a - self.a * other.b) / denom
        return Complex(real, imag)
    def mod(self):
        return Complex(math.sqrt(self.a**2 + self.b**2), 0)
    def __str__(self):
        return f"{self.a:.2f}{self.b:+.2f}i"

x = Complex(2, 1)
y = Complex(5, 6)

print("add:", x + y)
print("sub:", x - y)
print("mul:", x * y)
print("del:", x / y)
print("mod:", x.mod(), y.mod())
# задание 5 - тест 8

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

p3 = Point(3, 4)
p4 = Point(3, 4)
p5 = Point(7, 8)
print(p3 == p4)
print(p4 == p5)
print(hash(p3))
print(hash(p4))
print(hash(p5))
# задание 6 - тест 8