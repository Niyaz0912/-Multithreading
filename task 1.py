import threading


def find_max(numbers):
    """Функция для нахождения максимального значения в списке чисел.Параметры:
    numbers (list): Список чисел, в котором будет производиться поиск максимума.
    Возвращает:
    None: Результат выводится на экран.
    Выполняется 5 раз, каждый раз выводя текущее максимальное значение."""

    for i in range(5):
        max_value = max(numbers)
        print(f"Максимум: {max_value}")


def find_min(numbers):
    """Функция для нахождения минимального значения в списке чисел.
    Параметры:
    numbers (list): Список чисел, в котором будет производиться поиск минимума.
    Возвращает:
    None: Результат выводится на экран.
    Выполняется 5 раз, каждый раз выводя текущее минимальное значение."""

    for i in range(5):
        min_value = min(numbers)
        print(f"Минимум: {min_value}")


# Запросить у пользователя ввод значений для списка
while True:
    user_input = input("Введите числа через пробел: ")
    try:
        numbers_list = list(map(float, user_input.split()))
        break  # Выйти из цикла, если ввод корректен
    except ValueError:
        print("Пожалуйста, введите только числовые значения.")

# Создание потоков
max_thread = threading.Thread(target=find_max, args=(numbers_list,))
min_thread = threading.Thread(target=find_min, args=(numbers_list,))

# Запуск потоков
max_thread.start()
min_thread.start()

# Ожидание завершения потоков
max_thread.join()
min_thread.join()
