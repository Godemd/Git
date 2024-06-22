import json
import logging
import os
from typing import Any, List

import pandas as pd


def setup_logger(name: str) -> logging.Logger:
    """
    Настройка логгера.

    Аргументы:
        name (str): Имя логгера.

    Возвращает:
        logging.Logger: Объект логгера.
    """
    file_path = os.path.join("logs", f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s:%(lineno)d -> %(message)s")

    logger_file_handler = logging.FileHandler(file_path, encoding="utf-8", mode="w")
    logger_file_handler.setFormatter(formatter)

    logger.addHandler(logger_file_handler)

    return logger


logger = setup_logger("utils")


def read_data_from_json(file_path: str) -> List[Any]:
    """
    Возвращает список словарей из файла JSON, CSV или XLSX.

    Аргументы:
        file_path (str): Путь к файлу.

    Возвращает:
        list: Список словарей с данными из файла.
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл {file_path} не найден")
        return []

    if file_path.endswith(".json"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
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

    elif file_path.endswith(".csv"):
        try:
            df = pd.read_csv(file_path, delimiter=";")
            logger.info(f"Файл {file_path} успешно загружен")
            return df.to_dict("records")
        except Exception as e:
            logger.error(f"Ошибка при загрузке файла {file_path}: {e}")
            return []

    elif file_path.endswith(".xlsx"):
        try:
            df = pd.read_excel(file_path)
            logger.info(f"Файл {file_path} успешно загружен")
            return df.to_dict("records")
        except Exception as e:
            logger.error(f"Ошибка при загрузке файла {file_path}: {e}")
            return []

    else:
        logger.error(f"Неподдерживаемый формат файла {file_path}")
        return []


# Пример вызова функции
if __name__ == "__main__":
    file_path = "data\\transactions_excel.xlsx"  # Укажите путь к вашему файлу
    data = read_data_from_json(file_path)
    print(data)
