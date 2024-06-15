import json
import logging
import os


def setup_logger(name: str) -> logging.Logger:
    """
    ## Настройка логгера
    Аргументы:
        `name (str)`: Имя логгера
    Возвращает:
        `logging.Logger`: Объект логгера
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s:%(lineno)d -> %(message)s")
    logger_file_handler = logging.FileHandler(f"logs\\{name}.log", encoding="utf-8", mode="w")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    return logger


logger = setup_logger("utils")


def load_transactions(file_path: str) -> list:
    """
    ## Возвращает список словарей из JSON-строки
    Аргументы:
        `data_str (str)`: Путь к JSON-файлу
    Возвращает:
        `list`: список словарей
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл {file_path} не найден")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно загружен")
                return data
            else:
                logger.error(f"Файл {file_path} содержит некорректные данные")
                return []
        except json.JSONDecodeError:
            logger.error(f"Файл {file_path} содержит некорректные данные")
            return []

# Пример использования
# file_path = "data\operations.json"
# transactions = load_transactions(file_path)
# print("Загруженные транзакции:", transactions)
