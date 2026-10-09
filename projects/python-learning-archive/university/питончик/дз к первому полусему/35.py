# Рекурсивная функция обхода списка
def print_list_elements(lst, level=1):
    # lst — текущий список, level — уровень вложенности
    for element in lst:
        if isinstance(element, list):  # если элемент — список, углубляемся
            print_list_elements(element, level + 1)
        else:
            print(element, end=' ')
    # после вывода всех элементов на этом уровне выводим уровень
    print("level=", level)


# Пример ввода
numbers = [1, 2, [2, 3, 4, [3, 4, [2, 3], 5]]]

# Вызов функции
print_list_elements(numbers)