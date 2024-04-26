from collections import deque

def is_palindrome(input_string):
    # Перетворюємо рядок у нижній регістр та видаляємо пробіли
    input_string = input_string.lower().replace(" ", "")
    
    # Створюємо двосторонню чергу
    char_queue = deque()
    
    # Додаємо символи рядка до двосторонньої черги
    for char in input_string:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Приклад використання
test_string1 = "A man a plan a canal Panama" # Особлива подяка за цей рядок ChatGPT ;)
test_string2 = "hello"
test_string3 = "level"

print(is_palindrome(test_string1))  # Виведе: True
print(is_palindrome(test_string2))  # Виведе: False
print(is_palindrome(test_string3))  # Виведе: True
