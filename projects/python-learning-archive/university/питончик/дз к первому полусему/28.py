#1 прога

text = input()  # считываем строку
print(len(set(text)))  # множество хранит только уникальные символы

def count_unique_characters(texts):
    # Преобразуем строку в множество символов
    unique_chars = set(texts)
    # Длина множества = количество различных символов
    return len(unique_chars)

#2 прога

# Пример использования:
texts_1 = input("Введите текст: ")
print("Количество различных символов:", count_unique_characters(text))

