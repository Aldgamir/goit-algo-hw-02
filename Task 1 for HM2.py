import queue
import time
import random

# Створюємо чергу
request_queue = queue.Queue()

# Функція генерації заявок
def generate_request():
    # Генеруємо унікальний номер для заявки
    request_id = random.randint(1000, 1050) 
    # Створюємо заявку
    request = f"Request ID: {request_id}"
    # Додаємо заявку до черги
    request_queue.put(request)
    print(f"Заявка {request_id} додана до черги")

# Функція обробки заявок
def process_request():
    if not request_queue.empty():
        # Видаляємо заявку з черги
        request = request_queue.get()
        print(f"Заявка {request} оброблена")
    else:
        print("Черга порожня")

# Головний цикл програми
while True:
    # Генеруємо нові заявки
    generate_request()
    # Обробляємо заявки
    process_request()
    # Чекаємо певний час перед наступною ітерацією
    time.sleep(1) # Наприклад, чекати 1 секунду між кожною ітерацією
