import json
import os


def load_transactions(file_path: str) -> list:
    """
    Возвращает список словарей из JSON-строки, содержащей данные о финансовых транзакциях.

    Аргументы:
    file_path (str): Путь к файлу JSON.

    Возвращает:
    list: Список словарей с данными о финансовых транзакциях.

    Если файл не существует, возвращается пустой список.
    Если файл содержит некорректные данные или не может быть прочитан, также возвращается пустой список.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


# # Пример использования
# file_path = "data\operations.json"
# transactions = load_transactions(file_path)
# print("Загруженные транзакции:", transactions)
