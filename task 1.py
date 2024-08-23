import threading


# Функция для нахождения максимума
def find_max(numbers):
    for _ in range(5):
        max_value = max(numbers)
        print(f"Максимум: {max_value}")


# Функция для нахождения минимума
def find_min(numbers):
    for _ in range(5):
        min_value = min(numbers)
        print(f"Минимум: {min_value}")


# Запросить у пользователя ввод значений для списка
user_input = input("Введите числа через пробел: ")
numbers_list = list(map(float, user_input.split()))

# Создание потоков
max_thread = threading.Thread(target=find_max, args=(numbers_list,))
min_thread = threading.Thread(target=find_min, args=(numbers_list,))

# Запуск потоков
max_thread.start()
min_thread.start()

# Ожидание завершения потоков
max_thread.join()
min_thread.join()
