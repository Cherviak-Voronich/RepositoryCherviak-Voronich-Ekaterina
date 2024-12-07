import json    # Импортируем модуль
INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as f:
        python_obj = json.load(f)   # Десериализуем файл
    list_values = [(item["score"] * item["weight"]) for item in python_obj]     # Ищем значения произведений в каждом словаре
    sum_values = sum(list_values)   # Ищем сумму
    return round(sum_values, 3)     # Возвращаем сумму, округляя ее до 3 знаков после запятой

print(task())
