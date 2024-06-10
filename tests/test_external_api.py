import unittest
from unittest.mock import patch
from external_api import convert_transaction_amount, get_exchange_rate

class TestConvertTransactionAmount(unittest.TestCase):

    @patch('external_api.get_exchange_rate')
    def test_convert_transaction_amount_with_foreign_currency(self, mock_get_exchange_rate):
        # Создаем тестовые данные
        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD"
                }
            }
        }
        # Устанавливаем возвращаемое значение для mock_get_exchange_rate
        mock_get_exchange_rate.return_value = 7500.0  # Допустим, 100 USD = 7500 RUB

        # Вызываем функцию, которую тестируем
        result = convert_transaction_amount(transaction)

        # Проверяем, что функция get_exchange_rate была вызвана с правильными аргументами
        mock_get_exchange_rate.assert_called_once_with(100, "USD")

    def test_convert_transaction_amount_with_rub(self):
        # Создаем тестовые данные с валютой в рублях
        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "RUB"
                }
            }
        }

        # Вызываем функцию, которую тестируем
        result = convert_transaction_amount(transaction)

        # Проверяем, что результат соответствует ожидаемому значению
        self.assertEqual(result, 100.0)

if __name__ == '__main__':
    unittest.main()
