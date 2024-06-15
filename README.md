  # Git
**GitGit** - это проект на Python, предназначенный для упрощения задач обработки данных. Он предоставляет функции для фильтрации и сортировки списков словарей по определенным критериям.
- Были добавлены логи к модулям: `masks` и `utils` 
## Особенности
- **filter_by_state**: Фильтрует список словарей на основе значения ключа 'state'.
- **sort_by_date**: Сортирует список словарей по ключу 'date' в порядке возрастания или убывания.
## Использование
Примеры использования и демонстрации функциональности функции **filter_by_state**:
```python
def filter_by_state(dict_list: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    return [d for d in dict_list if d.get("state") == state]
# Пример использования функции
input_list = [
 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
output_desc = sort_by_date(input_list)
output_asc = sort_by_date(input_list, "asc")
print(output_desc)
print(output_asc)
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
>>> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
Примеры использования и демонстрации функциональности функции **sort_by_date**:
```python
def sort_by_date(dict_list: List[Dict[str, Any]], order: Optional[str] = "desc") -> List[Dict[str, Any]]:
    return sorted(dict_list, key=lambda x: x.get("date", ""), reverse=True if order == "asc" else False)
# Пример использования функции
input_list = [
 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
output_desc = sort_by_date(input_list)
output_asc = sort_by_date(input_list, "asc")
print(output_desc)
print(output_asc)
>>> [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
##Были добавлены новые модули utils и external_api
 Модуль utils.py 
содержит функцию get_data, которая предназначена для чтения и обработки данных из JSON-файла.

Функция get_data(путь к файлу: str) -> список
Функция get_data принимает путь к JSON-файлу в качестве аргумента и возвращает список словарей, представляющих данные о финансовых операциях.

Описание:

Открытие и чтение файла:

Функция открывает файл с помощью open(file_path, 'r', encoding='utf-8').
Файл открывается в режиме чтения ('r') с кодировкой utf-8.
Содержимое файла считывается с помощью file.read().
Проверка на пустой файл:

Функция проверяет, является ли файл пустым, используя not data.strip().
Если файл пустой, функция возвращает пустой список [].
Парсинг содержимого как JSON:

Функция использует json.loads(data) для преобразования считанного содержимого файла в список словарей.
Возврат данных:

Функция возвращает полученный список словарей, представляющих данные о финансовых операциях.
Пример использования:
```python
file_path = 'data/operations.json'
transactions = get_data(file_path)
print(transactions)
```
 Модуль external_api.pypy

Модуль external_api.py предоставляет функции для взаимодействия с внешним API для получения курсов валют и конвертации сумм транзакций.

Функции
get_api_request(url: str) -> requests.Response
Функция get_api_request отправляет GET-запрос к указанному URL и возвращает объект requests.Response, содержащий ответ от API.

Описание:

Отправка запроса:

Функция использует requests.get(url) для отправки GET-запроса к указанному URL.
Обработка ответа:

Функция проверяет статус-код ответа.
Если статус-код равен 200 (успешный ответ), функция возвращает объект requests.Response.
Если статус-код не равен 200, функция поднимает исключение requests.exceptions.HTTPError.
Пример использования:
```python
url = 'https://api.example.com/exchange_rates'
response = get_api_request(url)
print(response.status_code)
print(response.json())
```