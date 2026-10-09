from itertools import product
for i in product('F1?', repeat=2):
    print(''.join(i))
# задание 1 - тест 6

from itertools import islice

it = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
k = 3
while True:
    chunk = list(islice(it, k))
    if not chunk:
        break
    print(chunk)
# задание 2 - тест 6

class Iterator():
    def __init__(self, n):
        self.n = n
        self.currnt = 0
        self.cache = [0, 1]
    def __iter__(self):
        return self
    def __next__(self):
        if self.currnt >= self.n:
            raise StopIteration
        if self.currnt < len(self.cache):
            value = self.cache[self.currnt]
            self.currnt += 1
            return value
        new_value = self.cache[-1] + self.cache[-2]
        self.cache.append(new_value)
        self.currnt += 1
        return new_value

it_fib = Iterator(15)
for i in it_fib:
    print(i)
# задание 3 - тест 6

nums = [1, 4, 6, 2, 90, 53, 65, 25, 26, 88, 42]
gen = ([x, x%3] for x in nums)
for i in gen:
    print(*i)
# задание 4 - тест 6

def babylonian_sequence(a):
    x = 1.0
    while True:
        yield x
        x = 0.5 * (x + a / x)
        if abs(x*x - a) < 10**(-7):
            yield x
            break
for v in babylonian_sequence(7):
    print(v)
# задание 5 - тест 6

class UserMail():
    def __init__(self, login, email):
        self.login = login
        self._email = email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if isinstance(value, str) and value.count('@') == 1 and '.' in value.split('@')[1]:
            self._email = value
        else:
            print('Ошибочная почта!')

k = UserMail('kuzov', 'kuzovchikov@prepod.monster')
print(k.email)
k.email = [1, 2, 3]
k.email = 'kuzovchikov@not_prepod@.monster'
k.email = 'kuzovchikov@not_prepod.monster'
print(k.email)
# задание 6 - тест 6

class Money():
    def __init__(self, rubs, cops):
        self.total_cops = rubs*100 + cops
    @property
    def rubs(self):
        return self.total_cops // 100
    @rubs.setter
    def rubs(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cops = value*100 + self.cops
        else:
            print("Error rub")
    @property
    def cops(self):
        return self.total_cops % 100
    @cops.setter
    def cops(self, value):
        if isinstance(value, int) and value >= 0 and value < 100:
            self.total_cops = self.rubs*100 + value
        else:
            print("Error cops")
    def __str__(self):
        return f"Ваше состояние составляет {self.rubs} рублей {self.cops} копеек"

Dima = Money(101, 99)
print(Dima)
print(Dima.rubs, Dima.cops)
Dima.rubs = 666
print(Dima)
Dima.cops = 12
print(Dima)
# задание 7 - тест 6