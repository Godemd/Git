import json
import os
import tempfile

import pytest

from utils import load_transactions


@pytest.fixture
def valid_json_file():
    # Создаем временный файл с корректными данными JSON
    data = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(data)
        f.flush()
        yield f.name
    # Удаляем временный файл после завершения теста
    os.unlink(f.name)


@pytest.fixture
def invalid_json_file():
    # Создаем временный файл с некорректными данными JSON
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("invalid_json")
        f.flush()
        yield f.name
    # Удаляем временный файл после завершения теста
    os.unlink(f.name)


def test_load_transactions_existing_file(valid_json_file):
    # Проверяем, что функция успешно загружает данные из существующего файла
    transactions = load_transactions(valid_json_file)
    assert len(transactions) == 2
    assert isinstance(transactions[0], dict)


def test_load_transactions_nonexistent_file():
    # Проверяем, что функция возвращает пустой список при попытке загрузки из несуществующего файла
    transactions = load_transactions("nonexistent_file.json")
    assert transactions == []


def test_load_transactions_invalid_json(invalid_json_file):
    # Проверяем, что функция возвращает пустой список при попытке загрузки некорректного JSON
    transactions = load_transactions(invalid_json_file)
    assert transactions == []

