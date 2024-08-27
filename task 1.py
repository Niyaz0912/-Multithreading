import threading

# Список для хранения чисел
numbers = []

# События для синхронизации потоков
event_max = threading.Event()
event_min = threading.Event()

# Список для хранения результатов
results = []


def find_max():
    for i in range(5):
        # Ожидание события
        event_max.wait()
        if numbers:  # Проверяем, что список не пуст
            max_value = max(numbers)
            results.append(max_value)  # Сохраняем результат
        event_min.set()  # Устанавливаем событие для минимума
        event_max.clear()  # Сбрасываем событие для следующей итерации


def find_min():
    for i in range(5):
        # Ожидание события
        event_min.wait()
        if numbers:  # Проверяем, что список не пуст
            min_value = min(numbers)
            results.append(min_value)  # Сохраняем результат
        event_max.set()  # Устанавливаем событие для максимума
        event_min.clear()  # Сбрасываем событие для следующей итерации


def main():
    global numbers

    # Ввод чисел от пользователя
    while True:
        user_input = input("Введите числа через пробел: ")
        try:
            numbers = list(map(int, user_input.split()))  # Исправлено на присвоение
            break  # Выйти из цикла, если ввод корректен
        except ValueError:
            print("Пожалуйста, введите только числовые значения.")

    # Создание потоков
    thread_max = threading.Thread(target=find_max)
    thread_min = threading.Thread(target=find_min)

    # Запуск потоков
    thread_max.start()
    thread_min.start()

    # Начинаем с события для нахождения максимума
    event_max.set()

    # Ожидание завершения потоков
    thread_max.join()
    thread_min.join()

    # Вывод результатов
    print(" / ".join(map(str, results)))  # Преобразуем числа в строки для вывода


if __name__ == "__main__":
    main()