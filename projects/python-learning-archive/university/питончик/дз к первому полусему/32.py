def is_strong_password(password: str) -> bool:
    """
    Проверяет надежность пароля.
    Пароль считается надежным, если:
      - длина не менее 8 символов
      - содержит хотя бы одну заглавную букву
      - содержит хотя бы одну строчную букву
      - содержит хотя бы одну цифру
    """
    if len(password) < 8:
        return False

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    return has_upper and has_lower and has_digit


# Примеры использования:
print(is_strong_password("Qwerty12"))   # True — все условия выполняются
print(is_strong_password("qwerty12"))   # False — нет заглавных букв
print(is_strong_password("QWERTY12"))   # False — нет строчных букв
print(is_strong_password("Qwerty"))     # False — нет цифр и < 8 символов