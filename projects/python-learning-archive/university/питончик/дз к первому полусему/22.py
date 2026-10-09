def full_time(d):
    from datetime import timedelta
    # Импортируем timedelta для работы с разницами времени

    total = timedelta()
    # Инициализируем суммарное время total как нулевой объект timedelta

    for user, times in d.items():
        # Проходим по словарю, где key = пользователь, value = список из двух datetime
        start, end = times
        # Распаковываем список времени в начало и конец сессии
        total += (end - start)
        # Вычисляем длительность сессии (end - start) и добавляем к total

    # Переводим суммарное время total в секунды
    total_seconds = int(total.total_seconds())

    # Преобразуем секунды в часы, минуты и секунды
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Выводим результат в формате "X часов Y минут Z секунд"
    print(f"{hours} часов {minutes} минут {seconds} секунд")


# Пример использования:
from datetime import datetime

d = {
    "Alice": [datetime(2023, 10, 14, 9, 0, 0), datetime(2023, 10, 14, 12, 30, 0)],
    "Bob": [datetime(2023, 10, 14, 13, 0, 0), datetime(2023, 10, 14, 15, 45, 30)]
}

full_time(d)
# Ожидаемый вывод: "6 часов 15 минут 30 секунд"
