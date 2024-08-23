import threading

# Функция для нахождения суммы
def calculate_sum(numbers):
    for _ in range(5):
        total_sum = sum(numbers)
        print(f"Сумма: {total_sum}")

# Функция для нахождения среднеарифметического
def calculate_average(numbers):
    for _ in range(5):
        average = sum(numbers) / len(numbers) if numbers else 0
        print(f"Среднеарифметическое: {average}")

# Запросить у пользователя ввод значений для списка
user_input = input("Введите числа через пробел: ")
numbers_list = list(map(float, user_input.split()))

# Создание потоков
sum_thread = threading.Thread(target=calculate_sum, args=(numbers_list,))
average_thread = threading.Thread(target=calculate_average, args=(numbers_list,))

# Запуск потоков
sum_thread.start()
average_thread.start()

# Ожидание завершения потоков
sum_thread.join()
average_thread.join()