def make_biggest_number_simple(numbers):
    # Функция собирает из списка чисел наибольшее возможное "число" при конкатенации

    # Сортировка чисел по двум критериям:
    # 1) str(x)[0] — первая цифра числа (чтобы большие цифры шли вперёд)
    # 2) само число x — чтобы при одинаковой первой цифре большее число шло раньше
    # reverse=True — сортируем по убыванию
    sorted_nums = sorted(numbers, key=lambda x: (str(x)[0], x), reverse=True)

    # Преобразуем все числа в строки и объединяем в одно "число"
    return ''.join(map(str, sorted_nums))


#Примеры
print(make_biggest_number_simple([61, 228, 9]))   # 961228
print(make_biggest_number_simple([5, 204, 67]))   # 675204
print(make_biggest_number_simple([12, 3, 35, 2])) # 335212


def make_biggest_number(numbers):
    # Преобразуем числа в строки
    str_nums = list(map(str, numbers))

    n = len(str_nums)
    # Сортировка пузырьком по правилу "xy > yx"
    for i in range(n):
        for j in range(0, n - i - 1):
            if str_nums[j] + str_nums[j + 1] < str_nums[j + 1] + str_nums[j]:
                # Меняем местами
                str_nums[j], str_nums[j + 1] = str_nums[j + 1], str_nums[j]

    # Объединяем в одно число
    result = ''.join(str_nums)

    # Если результат начинается с нуля, значит все числа были нулями
    return result.lstrip('0') or '0'


# Примеры
print(make_biggest_number([61, 228, 9]))  # 961228
print(make_biggest_number([5, 204, 67]))  # 675204
print(make_biggest_number([12, 121]))  # 12121
print(make_biggest_number([824, 82]))  # 82824
print(make_biggest_number([3, 30, 34, 5, 9]))  # 9534330
print(make_biggest_number([0, 0, 0]))  # 0
