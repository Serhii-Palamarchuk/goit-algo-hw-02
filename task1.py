# Завдання 1
# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати 
# нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", 
# імітуючи таким чином роботу сервісного центру.

import queue
import random
import time

# Створюємо чергу для заявок
requests_queue = queue.Queue()

# Лічильник заявок
request_id = 1

# Функція для генерації нової заявки
def generate_request():
    global request_id
    new_request = f"Request-{request_id}"
    request_id += 1
    requests_queue.put(new_request)
    print(f"Generated new request: {new_request}")

# Функція для обробки заявки
def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Processing {request}...")
        # Імітація обробки заявки
        time.sleep(1)
        print(f"Completed processing {request}")
    else:
        print("No requests to process.")

# Головний цикл програми
def main():
    while True:
        # Генерація нової заявки кожні 2 секунди
        generate_request()
        time.sleep(random.uniform(0.5, 1.5))  # Імітуємо непостійний час між заявками

        # Обробка заявки
        process_request()
        time.sleep(1)  # Пауза перед обробкою наступної заявки

        # Для зупинки програми можна додати умовний вихід, наприклад, після 10 заявок
        if request_id > 10:
            print("Simulation finished.")
            break

if __name__ == "__main__":
    main()
