import tracemalloc
import time
def unslotted_fn():
    class UnSlottedClass:
        def __init__(self, i):
            self.value = i

    unslotted = []
    for i in range(1_000_000):
        unslotted.append(UnSlottedClass(i))
    return unslotted

def slotted_fn():
    class UnSlottedClass:
        __slots__ = ('value',)
        def __init__(self, i):
            self.value = i

    slotted = []
    for i in range(1_000_000):
        slotted.append(UnSlottedClass(i))
    return slotted

tracemalloc.start() #эта библиотека потому-что та, что дана в задании не работала.
start_time = time.time()
unslotted_fn()
print(f'В пике {tracemalloc.get_traced_memory()[1]} МБ, за {time.time()-start_time:.4f} cекунд')
tracemalloc.stop()
print('')
tracemalloc.start()
start_time = time.time()
slotted_fn()
print(f'В пике {tracemalloc.get_traced_memory()[1]} МБ, за {time.time()-start_time:.4f} cекунд')
tracemalloc.stop()
# задание 1 - тест 9

class Roditel1:
    __slots__ = ()
class Roditel2:
    __slots__ = ()

class Do4erniy(Roditel1, Roditel2):
    __slots__ = ('slot1', 'slot2')
    def __init__(self, slot1, slot2):
        self.slot1 = slot1
        self.slot2 = slot2

d = Do4erniy(10, 20)
print(d.slot1, d.slot2)
# задание 2 - тест 9

from enum import *
class Weapon(Enum):
    SWORD = 1
    BOW = 2
    DAGGER = 3
    CLUB = 4
for i in Weapon:
    print(i.name, i.value)
# задание 3 - тест 9

from enum import *
names = "SWORD BOW DAGGER CLUB"
Weapon = Enum('Weapon', names, start=12)

for i in Weapon:
    print(i.name, i.value)
# задание 4 - тест 9

from enum import *
class Weapon(Enum):
    SWORD = auto()
    BOW = auto()
    DAGGER = auto()
    CLUB = auto()
for i in Weapon:
    print(i.name, i.value)
# задание 5 - тест 9

from enum import *
@unique
class Weapon(Enum):
    SWORD = 1
    BOW = 2
    DAGGER = 3
    CLUB = 1 # <- говно
for i in Weapon:
    print(i.name, i.value)
# задание 6 - тест 9

from enum import *
class ienum(IntEnum):
    alpha = 93
    beta = 355
    gamma = 213
    delta = 376
    iota = 244
    kappa = 672
for i in sorted(ienum):
    print(i.name, i.value)
# задание 7 - тест 9

from dataclasses import dataclass
@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.age}) - {self.job}'
    def serialize(self, type):
        if type == 'dict':
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
                'job': self.job
            }
        elif type == 'tuple':
            return (self.first_name, self.last_name, self.age, self.job)
        else:
            raise ValueError('Доступно только: dict, tuple')

Dima = Person('Dima', 'Kuzov', 25, 'Data Scientist')
print(Dima)
print(Dima.serialize('dict'))
print(Dima.serialize('tuple'))
# задание 8 - тест 9

@dataclass
class newPerson(Person):
    def __post_init__(self):
        self.full_name = f'{self.first_name} {self.last_name}'
    def __str__(self):
        return f'{self.full_name} ({self.age}) - {self.job}'
    def serialize(self, type):
        if type == 'dict':
            data = super().serialize('dict')
            data['full_name'] = self.full_name
            return data
        elif type == 'tuple':
            return (*super().serialize('tuple'), self.full_name)
        else:
            raise ValueError('Доступно только: dict, tuple')
Dima = newPerson('Dima', 'Kuzov', 25, 'Data Scientist')
print(Dima)
print(Dima.serialize('dict'))
print(Dima.serialize('tuple'))
# задание 9 - тест 9

class Value():
    def __get__(self, instance, owner):
        return instance.__dict__.get('_amount', 0.0)
    def __set__(self, instance, value):
        commission = getattr(instance, 'commission', 0.0)
        instance.__dict__['_amount'] = value * (1 - commission)
class Account():
    amount = Value()
    def __init__(self, commission):
        self.commission = commission

acc = Account(0.05)
acc.amount = 1000
print(acc.amount)
# задание 10 - тест 9

class Fuel_cap():
    def __get__(self, instance, owner):
        return instance.__dict__.get('fuel_cap')
    def __set__(self, instance, value):
        if isinstance(value, int) and value > 0:
            instance.__dict__['fuel_cap'] = value
        elif value <= 0:
            raise ValueError('Fuel Capacity can never be less than zero')
        else:
            raise TypeError('Fuel Capacity can only be an integer')
    def __delete__(self, instance):
        if 'fuel_cap' in instance.__dict__:
            del instance.__dict__['fuel_cap']
class Car():
    fuel_cap = Fuel_cap()
    def __init__(self, maker, model, fuel_cap):
        self.maker = maker
        self.model = model
        self.fuel_cap = fuel_cap
    def __str__(self):
        return f'{self.maker} model {self.model} with a fuel capacity of {self.fuel_cap} ltr.'

car1 = Car("BMW","X7",40)
print(car1)
print(car1.__dict__)
del car1.fuel_cap
print(car1.__dict__)
car2 = Car("BMW","X7",-40)
car3 = Car("BMW","X7",40.4)
# задание 11 - тест 9