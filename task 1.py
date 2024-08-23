import threading

# Переменные для хранения значений
max_value = None
min_value = None


def find_max(numbers):
    """Функция для нахождения максимального значения в списке чисел.
    Параметры:
    numbers (list): Список чисел, в котором будет производиться поиск максимума.
    Возвращает:
    None"""
    global max_value
    max_value = max(numbers)  # Находим максимум


def find_min(numbers):
    """Функция для нахождения минимального значения в списке чисел.
    Параметры:
    numbers (list): Список чисел, в котором будет производиться поиск минимума.
    Возвращает:
    None"""
    global min_value
    min_value = min(numbers)  # Находим минимум


# Запросить у пользователя ввод значений для списка
while True:
    user_input = input("Введите числа через пробел: ")
    try:
        numbers_list = list(map(int, user_input.split()))
        break  # Выйти из цикла, если ввод корректен
    except ValueError:
        print("Пожалуйста, введите только числовые значения.")

# Создание потоков
thread_1 = threading.Thread(target=find_max, args=(numbers_list,))
thread_2 = threading.Thread(target=find_min, args=(numbers_list,))

# Запуск потоков
thread_1.start()
thread_2.start()

# Ожидание завершения потоков
thread_1.join()
thread_2.join()

# Цикл для вывода значений поочередно
for _ in range(5):
    print(f"{max_value}/{min_value}", end="")
    if _ < 4:
        print("/", end="")

print()
