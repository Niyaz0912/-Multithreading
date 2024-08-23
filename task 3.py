import random
import threading


def fill_list(size):
    """Функция для заполнения списка случайными числами.
    Параметры:
    size (int): Количество случайных чисел, которые нужно сгенерировать.
    Возвращает:
    list: Список случайных чисел."""
    return [random.randint(1, 100) for _ in range(size)]


def calculate_sum(numbers):
    """Функция для вычисления суммы элементов в списке чисел.
    Параметры:
    numbers (list): Список чисел, для которого будет вычисляться сумма.
    Возвращает:
    int: Сумма элементов в списке."""
    return sum(numbers)


def calculate_average(numbers):
    """Функция для вычисления среднеарифметического значения элементов в списке чисел.
    Параметры:
    numbers (list): Список чисел, для которого будет вычисляться среднеарифметическое.
    Возвращает:
    float: Среднеарифметическое значение элементов в списке. Если список пуст, возвращает 0."""
    return sum(numbers) / len(numbers) if numbers else 0


# Определяем размер списка
size = 10

# Переменные для хранения результатов
filled_list = []
sum_result = 0
average_result = 0

# Флаг для синхронизации
list_filled = threading.Event()


def thread_fill_list():
    """Потоковая функция для заполнения списка случайными числами.
    После заполнения списка устанавливает флаг."""
    global filled_list
    filled_list = fill_list(size)
    list_filled.set()  # Устанавливаем флаг, что список заполнен


def thread_sum():
    """Потоковая функция для вычисления суммы элементов списка.
    Ожидает, пока список не будет заполнен."""
    list_filled.wait()  # Ожидание заполнения списка
    global sum_result
    sum_result = calculate_sum(filled_list)


def thread_average():
    """Потоковая функция для вычисления среднеарифметического значения элементов списка.
    Ожидает, пока список не будет заполнен."""
    list_filled.wait()  # Ожидание заполнения списка
    global average_result
    average_result = calculate_average(filled_list)


# Создание потоков
fill_thread = threading.Thread(target=thread_fill_list)
sum_thread = threading.Thread(target=thread_sum)
average_thread = threading.Thread(target=thread_average)

# Запуск потоков
fill_thread.start()
sum_thread.start()
average_thread.start()

# Ожидание завершения потоков
fill_thread.join()
sum_thread.join()
average_thread.join()

# Вывод результатов
print(f"Список: {filled_list}")
print(f"Сумма: {sum_result}")
print(f"Среднеарифметическое: {average_result}")
