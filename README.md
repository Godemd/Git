 # Git

**Git** - это проект на Python, предназначенный для упрощения задач обработки данных. Он предоставляет функции для фильтрации и сортировки списков словарей по определенным критериям.

## Особенности

- **filter_by_currency(transactions, currency)**: Фильтрует список транзакций по указанной валюте.
- **transaction_descriptions(transactions)**: Генерирует список описаний для каждой транзакции в предоставленном списке.
- **card_number_generator(start, end)**: Генерирует список номеров карт в формате XXXX XXXX XXXX XXXX в указанном диапазоне.
## Использование

Эти функции могут быть использованы для обработки и генерации данных, связанных с транзакциями и номерами карт. Например, вы можете использовать filter_by_currency для фильтрации списка транзакций по транзакциям в определенной валюте, или использовать transaction_descriptions для генерации списка описаний для каждой транзакции.

```python
def filter_by_state(dict_list: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    return [d for d in dict_list if d.get("state") == state]

# Пример использования функции
# Фильтрация транзакций по валюте
transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}},
]
filtered_transactions = filter_by_currency(transactions, "USD")
```
# Генерация описаний транзакций
descriptions = transaction_descriptions(transactions)

# Генерация номеров карт
card_numbers = card_number_generator(1000000000000000, 1000000000000009)
 
 ##test_generators.py
Этот файл содержит модульные тесты для функций, определенных в src/generators.py.

##Тестируемые функции
- **card_number_generator**: Эта функция генерирует последовательность номеров кредитных карт на основе начального и конечного номеров.
- **filter_by_currency**: Эта функция фильтрует список транзакций по валюте суммы транзакции.
- **transaction_descriptions**: Эта функция извлекает описания из списка транзакций.
##Тесты
Каждая функция имеет несколько тестов, которые охватывают различные сценарии. Например, функция card_number_generator тестируется с разными начальными и конечными номерами, а функция filter_by_currency тестируется с разными валютами.

##Утверждения
Каждый тест использует утверждения для проверки того, что функция работает как ожидается. Например, тест card_number_generator утверждает, что сгенерированный список номеров карт равен ожидаемому списку.

##Документация
Файл включает в себя docstrings для каждой функции и теста. Docstrings предоставляют краткое описание функции или теста и его назначение.

# Тесты
```
@pytest.mark.parametrize("currency,expected_count", [
    ("USD", 3),
    ("RUB", 2),
    ("EUR", 0)
])
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count

@pytest.mark.parametrize("expected_descriptions", [
    [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
])
def test_transaction_descriptions(transactions, expected_descriptions):
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions

@pytest.mark.parametrize("start,end,expected_cards", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]),
    (10, 12, [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012"
    ])
])
def test_card_number_generator(start, end, expected_cards):
    result = list(card_number_generator(start, end))
    assert result == expected_cards

```