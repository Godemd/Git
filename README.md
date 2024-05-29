 # Git

**Git** - это проект на Python, предназначенный для упрощения задач обработки данных. Он предоставляет функции для фильтрации и сортировки списков словарей по определенным критериям.

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

<<<<<<< Updated upstream
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
=======
```
## Особенности
- **log** Декоратор для логирования вызовов функций и их результатов.
- Простота использования: Декоратор log прост в использовании. Вам нужно всего лишь добавить его перед функцией, которую вы хотите логировать.
- Настраиваемый: Вы можете указать имя файла, в который будут записываться логи. Если имя файла не указано, логи будут выводиться в консоль.
- Гибкий: Декоратор log может быть использован для логирования различных типов информации, включая имя функции, аргументы, результаты и исключения.
#Пример использования
```
@log("function_calls.log")
def my_function(x, y):
    return x + y

result = my_function(1, 2)
```
В этом примере декоратор log запишет информацию о вызове функции my_function в файл function_calls.log. Запись будет выглядеть следующим образом:
```
my_function ok
```
Если функция my_function вызовет исключение, декоратор log запишет информацию об исключении в файл function_calls.log. Запись будет выглядеть следующим образом:
```
my_function error: ZeroDivisionError. Inputs: (1, 0)
>>>>>>> Stashed changes
```