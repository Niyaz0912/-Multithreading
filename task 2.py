import threading

# Переменные для хранения значений
total_sum = 0
average_value = 0.0

# Создаем события для синхронизации потоков
event_sum = threading.Event()
event_average = threading.Event()


def calculate_sum(numbers):
    """Функция для вычисления суммы чисел в списке.
    Параметры:
    numbers (list): Список чисел, для которых будет вычисляться сумма.
    Возвращает:
    None"""
    global total_sum
    total_sum = sum(numbers)  # Находим сумму


def calculate_average(numbers):
    """Функция для вычисления среднеарифметического значения чисел в списке.
    Параметры:
    numbers (list): Список чисел, для которых будет вычисляться среднеарифметическое.
    Возвращает:
    None"""
    global average_value
    if numbers:  # Проверяем, что список не пуст
        average_value = sum(numbers) / len(numbers)  # Находим среднее
    else:
        average_value = 0.0  # Если список пуст, среднее равно 0


# Запросить у пользователя ввод значений для списка
while True:
    user_input = input("Введите числа через пробел: ")
    try:
        numbers_list = list(map(int, user_input.split()))
        break  # Выйти из цикла, если ввод корректен
    except ValueError:
        print("Пожалуйста, введите только числовые значения.")

# Создание потоков
thread_1 = threading.Thread(target=calculate_sum, args=(numbers_list,))
thread_2 = threading.Thread(target=calculate_average, args=(numbers_list,))

# Запуск потоков
thread_1.start()
thread_2.start()

# Ожидание завершения потоков
thread_1.join()
thread_2.join()

# Цикл для вывода значений поочередно
for _ in range(5):
    print(f"{total_sum}", end="")
    event_average.set()  # Сигнализируем, что сумма была выведена
    event_sum.clear()  # Ожидаем, пока среднее не будет выведено
    event_average.wait()  # Ждем, пока среднее не будет выведено
    print("/", end="")

    print(f"{average_value:.2f}", end="")
    event_sum.set()  # Сигнализируем, что среднее было выведено
    event_average.clear()  # Ожидаем, пока сумма не будет выведена
    event_sum.wait()  # Ждем, пока сумма не будет выведена
    if _ < 4:
        print("/", end="")

print()
