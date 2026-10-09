# Ввод списка чисел
numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

# Создаём пустой словарь
divisors_dict = {}

# Для каждого числа находим список его делителей
for num in numbers:
    divisors = []              # сюда будем собирать делители
    for i in range(1, num + 1):
        if num % i == 0:       # если i делит num без остатка
            divisors.append(i)
    divisors_dict[num] = divisors  # добавляем в словарь

# Выводим результат
print(divisors_dict)