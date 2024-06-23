import unittest.mock as mock

import pandas as pd

# Импортируем функции для тестирования
from src.utils import read_transactions_csv, read_transactions_excel, read_transactions_json


def mock_pd_read_csv(file_path, delimiter=";"):
    # Заглушка для эмуляции pd.read_csv
    return pd.DataFrame([{"col1": 1, "col2": "data1"}, {"col1": 2, "col2": "data2"}])


def mock_pd_read_excel(file_path):
    # Заглушка для эмуляции pd.read_excel
    return pd.DataFrame([{"col1": 1, "col2": "data1"}, {"col1": 2, "col2": "data2"}])


def mock_pd_read_json(file_path):
    # Заглушка для эмуляции pd.read_json
    return pd.DataFrame([{"col1": 1, "col2": "data1"}, {"col1": 2, "col2": "data2"}])


@mock.patch("src.utils.pd.read_csv", side_effect=mock_pd_read_csv)
def test_read_transactions_csv(mock_read_csv):
    # Тестирование read_transactions_csv
    file_path = "dummy.csv"

    result = read_transactions_csv(file_path)
    expected = [{"col1": 1, "col2": "data1"}, {"col1": 2, "col2": "data2"}]
    assert result == expected


@mock.patch("src.utils.pd.read_excel", side_effect=mock_pd_read_excel)
def test_read_transactions_excel(mock_read_excel):
    # Тестирование read_transactions_excel
    file_path = "dummy.xlsx"

    result = read_transactions_excel(file_path)
    expected = [{"col1": 1, "col2": "data1"}, {"col1": 2, "col2": "data2"}]
    assert result == expected


@mock.patch("src.utils.pd.read_json", side_effect=mock_pd_read_json)
def test_read_transactions_json(mock_read_json):
    # Тестирование read_transactions_json
    file_path = "dummy.json"

    result = read_transactions_json(file_path)
    expected = [{"col1": 1, "col2": "data1"}, {"col1": 2, "col2": "data2"}]
    assert result == expected


if __name__ == "__main__":
    unittest.main()
