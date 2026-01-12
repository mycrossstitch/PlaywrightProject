import random
import string
from typing import Optional

from faker import Faker

fake = Faker()


SPECIALS = "!@#$%^&*"


def generate_test_string(is_valid: bool = True, length: Optional[int] = None) -> str:
    """
    Генерирует тестовую строку для проверки поля.

    Args:
        is_valid: True для валидной строки, False для невалидной
        length: Желаемая длина строки (если None - случайная от 2 до 25)

    Returns:
        Тестовая строка
    """
    # Валидные символы согласно требованиям
    valid_chars = string.ascii_letters + string.digits + "_-"

    # Невалидные символы
    invalid_chars = "!@#$%^&*()+={}[]|\\:;\"'<>,.?/ "

    # Определяем длину строки
    if length is None:
        # Случайная длина от 2 до 25
        length = random.randint(2, 25)

    # Обработка крайних случаев длины
    if length <= 0:
        return ""  # Пустая строка для length = 0

    if is_valid:
        # Генерация валидной строки
        # Все символы должны быть из valid_chars
        return "".join(random.choices(valid_chars, k=length))

    else:
        # Генерация невалидной строки
        # Должен быть хотя бы один невалидный символ
        # Строка не может начинаться с пробела

        if length == 1:
            # Для длины 1 просто возвращаем невалидный символ (не пробел)
            non_space_invalid = invalid_chars.replace(" ", "")
            return random.choice(non_space_invalid)

        # Для длины >= 2
        # Определяем позицию для невалидного символа (не первый символ, если это пробел)
        invalid_pos = random.randint(0, length - 1)

        # Создаем список символов
        chars = []

        for i in range(length):
            if i == invalid_pos:
                # На этой позиции должен быть невалидный символ
                # Если это первая позиция, исключаем пробел
                if i == 0:
                    invalid_without_space = invalid_chars.replace(" ", "")
                    chars.append(random.choice(invalid_without_space))
                else:
                    chars.append(random.choice(invalid_chars))
            else:
                # Остальные позиции могут быть любыми символами
                all_chars = valid_chars + invalid_chars
                char = random.choice(all_chars)

                # Если это первая позиция и выбран пробел, выбираем другой символ
                if i == 0 and char == " ":
                    all_chars_without_space = all_chars.replace(" ", "")
                    char = random.choice(all_chars_without_space)

                chars.append(char)

        return "".join(chars)


def generate_valid_password(min_length=8):
    """
    Generates a password that satisfies:
    - at least 1 upper
    - at least 1 lower
    - at least 1 digit
    - at least 1 special
    - length >= min_length
    """

    # гарантируем выполнение правил
    password_chars = [
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        random.choice("abcdefghijklmnopqrstuvwxyz"),
        random.choice("0123456789"),
        random.choice(SPECIALS),
    ]

    # добираем до минимальной длины
    remaining = max(min_length - len(password_chars), 0)
    password_chars += [
        fake.random_element(
            elements="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            + SPECIALS
        )
        for _ in range(remaining)
    ]

    # перемешиваем, чтобы не было шаблона
    random.shuffle(password_chars)

    return "".join(password_chars)
