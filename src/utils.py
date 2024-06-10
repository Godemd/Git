import json

def get_data(file_path: str) -> list:
    # Открытие и чтение файла
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        
        # Проверка на пустой файл
        if not data.strip():
            return []
        
        # Парсинг содержимого как JSON
        transaction = json.loads(data)
        
        return transaction

# # Пример использования функции
# file_path = 'data/operations.json'
# transactions = get_data(file_path)
# print(transactions)
