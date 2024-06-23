import logging
import os
from typing import Union

import pandas as pd


def setup_logger(name: str) -> logging.Logger:
    """
    ## Настройка логгера
    Аргументы:
        `name (str)`: Имя логгера
    Возвращает:
        `logging.Logger`: Объект логгера
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


def read_transactions_csv(file_path: str) -> list:
    """
    Считывает финансовые транзакции из CSV-файла.

    Аргументы:
    - file_path (str): Путь к CSV-файлу.

    Возвращает:
    - Union[list, None]: Список словарей с транзакциями или None в случае ошибки.
    """
    try:
        logger.info(f"Чтение CSV файла: {file_path}")
        return pd.read_csv(file_path, delimiter=";").to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV файла '{file_path}': {e}")
        return []


def read_transactions_excel(file_path: str) -> list:
    """
    Считывает финансовые транзакции из Excel-файла.

    Аргументы:
    - file_path (str): Путь к Excel-файлу.

    Возвращает:
    - Union[list, None]: Список словарей с транзакциями или None в случае ошибки.
    """
    try:
        logger.info(f"Чтение Excel файла: {file_path}")
        return pd.read_excel(file_path).to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel файла '{file_path}': {e}")
        return []


def read_transactions_json(file_path: str) -> list:
    """
    Считывает финансовые транзакции из JSON-файла.

    Аргументы:
    - file_path (str): Путь к JSON-файлу.

    Возвращает:
    - Union[list, None]: Список словарей с транзакциями или None в случае ошибки.
    """
    try:
        logger.info(f"Чтение JSON файла: {file_path}")
        return pd.read_json(file_path).to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка при чтении JSON файла '{file_path}': {e}")
        return []


# Чтение транзакций из Excel файла
excel_file_path = "data\transactions_excel.xlsx"
transactions_excel = read_transactions_excel(excel_file_path)
print(transactions_excel)
