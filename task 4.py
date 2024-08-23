import random
import threading
import os


def fill_file(file_path, size):
    """
    Функция для заполнения файла случайными числами.

    Параметры:
    file_path (str): Путь к файлу, который будет заполнен.
    size (int): Количество случайных чисел, которые нужно записать в файл.

    Возвращает:
    None
    """
    with open(file_path, 'w') as f:
        for _ in range(size):
            f.write(f"{random.randint(1, 100)}\n")


def is_prime(num):
    """
    Функция для проверки, является ли число простым.

    Параметры:
    num (int): Число для проверки.

    Возвращает:
    bool: True, если число простое, иначе False.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def calculate_factorial(num):
    """
    Функция для вычисления факториала числа.

    Параметры:
    num (int): Число для вычисления факториала.

    Возвращает:
    int: Факториал числа.
    """
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def find_primes(file_path, output_file):
    """
    Функция для нахождения простых чисел в файле и записи их в новый файл.

    Параметры:
    file_path (str): Путь к входному файлу.
    output_file (str): Путь к выходному файлу для записи простых чисел.

    Возвращает:
    None
    """
    primes = []
    with open(file_path, 'r') as f:
        for line in f:
            num = int(line.strip())
            if is_prime(num):
                primes.append(num)

    with open(output_file, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")

    print(f"Найдено простых чисел: {len(primes)}. Результаты записаны в {output_file}.")


def calculate_factorials(file_path, output_file):
    """
    Функция для вычисления факториала чисел из файла и записи результатов в новый файл.

    Параметры:
    file_path (str): Путь к входному файлу.
    output_file (str): Путь к выходному файлу для записи факториалов.

    Возвращает:
    None
    """
    factorials = []
    with open(file_path, 'r') as f:
        for line in f:
            num = int(line.strip())
            factorials.append(calculate_factorial(num))

    with open(output_file, 'w') as f:
        for fact in factorials:
            f.write(f"{fact}\n")

    print(f"Факториалы вычислены для {len(factorials)} чисел. Результаты записаны в {output_file}.")


# Запросить у пользователя путь к файлу
file_path = input("Введите путь к файлу для заполнения: ")
size = 10  # Количество случайных чисел

# Заполнение файла случайными числами
fill_thread = threading.Thread(target=fill_file, args=(file_path, size))
fill_thread.start()
fill_thread.join()  # Ожидание завершения заполнения файла

# Создание потоков для нахождения простых чисел и вычисления факториалов
primes_output_file = os.path.splitext(file_path)[0] + "_primes.txt"
factorials_output_file = os.path.splitext(file_path)[0] + "_factorials.txt"

primes_thread = threading.Thread(target=find_primes, args=(file_path, primes_output_file))
factorials_thread = threading.Thread(target=calculate_factorials, args=(file_path, factorials_output_file))

# Запуск потоков
primes_thread.start()
factorials_thread.start()

# Ожидание завершения потоков
primes_thread.join()
factorials_thread.join()

# Статистика выполненных операций
print(f"Заполнение файла: {file_path} завершено.")
print(f"Простые числа записаны в: {primes_output_file}")
print(f"Факториалы записаны в: {factorials_output_file}")
