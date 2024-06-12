from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """
    Функция принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.

    Args:
        transactions: Список словарей с банковскими операциями.
        currency: Валюта, по которой нужно фильтровать операции.

    Returns:
        Итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Функция принимает список словарей с банковскими операциями и возвращает генератор,
    который выдает описание каждой операции по очереди.

    Args:
        transactions: Список словарей с банковскими операциями.

    Returns:
        Генератор, который выдает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Функция принимает диапазон номеров карт и возвращает генератор,
    который генерирует номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра.

    Args:
        start: Начальный номер карты в диапазоне.
        end: Конечный номер карты в диапазоне.

    Returns:
        Генератор, который генерирует номера карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        card_number = f"{number:016}"  # Форматируем номер как 16-значное число с лидирующими нулями
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
