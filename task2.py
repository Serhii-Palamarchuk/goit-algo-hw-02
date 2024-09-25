# Завдання 2
# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи 
# до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, 
# щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
# а також бути нечутливою до регістру та пробілів.
from collections import deque

# Функція для перевірки, чи є рядок паліндромом
def is_palindrome(input_string):
    # Видаляємо пробіли та перетворюємо рядок у нижній регістр
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Додаємо символи до двосторонньої черги
    char_deque = deque(cleaned_string)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не співпадають, це не паліндром

    return True  # Якщо всі символи співпадають, це паліндром

# Тестування функції
test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
]

for string in test_strings:
    result = is_palindrome(string)
    print(f"'{string}' is a palindrome: {result}")
