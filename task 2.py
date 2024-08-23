import threading


def calculate_sum(numbers):
    """Функция для вычисления суммы элементов в списке чисел.
    Параметры:
    numbers (list): Список чисел, для которого будет вычисляться сумма.
    Возвращает:
    None: Результат выводится на экран.
    Выполняется 5 раз, каждый раз выводя текущую сумму элементов."""

    for _ in range(5):
        total_sum = sum(numbers)
        print(f"Сумма: {total_sum}")


def calculate_average(numbers):
    """Функция для вычисления среднеарифметического значения элементов в списке чисел.
    Параметры:
    numbers (list): Список чисел, для которого будет вычисляться среднеарифметическое.
    Возвращает:
    None: Результат выводится на экран.
    Выполняется 5 раз, каждый раз выводя текущее среднеарифметическое значение.
    Если список пуст, выводится 0."""

    for _ in range(5):
        average = sum(numbers) / len(numbers) if numbers else 0
        print(f"Среднеарифметическое: {average}")


# Запросить у пользователя ввод значений для списка
while True:
    user_input = input("Введите числа через пробел: ")
    try:
        numbers_list = list(map(float, user_input.split()))
        break  # Выйти из цикла, если ввод корректен
    except ValueError:
        print("Пожалуйста, введите только числовые значения.")

# Создание потоков
sum_thread = threading.Thread(target=calculate_sum, args=(numbers_list,))
average_thread = threading.Thread(target=calculate_average, args=(numbers_list,))

# Запуск потоков
sum_thread.start()
average_thread.start()

# Ожидание завершения потоков
sum_thread.join()
average_thread.join()