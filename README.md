# Проект "Виджет банковских операций"

## Описание:

IT-отдел крупного банка делает новую фичу для личного кабинета клиента.
Это виджет, который показывает несколько последних успешных банковских
операций клиента.

## Установка:

1. На сайте GitHub, на странице проекта, нажмите кнопку Code. В выпадающем меню скопируйте HTTPS-ключ
2. В главном меню PyCharm перейдите в меню Get from VCS
3. Вставьте ссылку на репозиторий и нажмите на кнопку Clone

4. или Используйте команду git clone <HTTPS-ключ>

## Использование:

В докстрингах вы можете увидеть описание функций

Примеры использования функций из masks.py
```
from src.masks import get_mask_card_number, get_mask_account


print(get_mask_card_number('1234567891234567'))
>>> 1234 56** **** 4567

print(get_mask_account('12345678912345678912'))
>>> **8912
```

Примеры использования функций из processing.py:
```
from src.processing import filter_by_state, sort_by_date


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
                       
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
     
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))                       

>>> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
     
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
                    
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
     
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], False))     

>>> [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

```

Примеры использования функций из generators.py
```
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

print(next(usd_transactions))
>>> {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    
print(next(usd_transactions))
>>> {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    

descriptions = transaction_descriptions(transactions)

print(next(descriptions))
>>> Перевод организации

print(next(descriptions))
>>> Перевод со счета на счет


card_number = card_number_generator(1, 5)

for x in range(5):
    print(next(card_number))
>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005    
```
Примеры использования функций из decorators.py

`@log()` с параметром `filename` по умолчанию
```
@log()
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в консоль при успешном выполнении:
# >>> my_function ok

# Ожидаемый вывод при ошибке:
# >>> my_function error: тип ошибки. Inputs: (1, 2), {}

```
`@log()` с параметром `filename` = `"mylog.txt"`
```
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# >>> my_function ok

# Ожидаемый вывод при ошибке:
# >>> my_function error: тип ошибки. Inputs: (1, 2), {}

```
Примеры использования функций из read_csv_xlsx_files.py:
```
from src.read_csv_xlsx_files import read_csv_file, read_excel_file


print(read_csv_file("data/example.csv"))
>>>  [{"name": "Иван", "age": "25", "city": "Москва"}, {"name": "Мария", "age": "30", "city": "СПб"}]

print(read_excel_file("data/example.xlsx"))
>>>  [{"name": "Иван", "age": "25", "city": "Москва"}, {"name": "Мария", "age": "30", "city": "СПб"}]
```
Примеры использования функций из process_bank.py:
```
from src.process_bank import process_bank_search_description, process_bank_operations


print(process_bank_search_description(transactions, 'организации'))
>>> [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
]

print(process_bank_operations(transactions, "Перевод организации"))
>>>  {"Перевод организации": 5, "Перевод со счета на счет": 7}
```
Примеры использования main из main.py:
```
# Программа приветствует пользователя:

Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Пользователь: 1

Программа: Для обработки выбран JSON-файл.

# После пользователь выбирает статус интересующих его операций.

Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Пользователь: EXECUTED

Программа: Операции отфильтрованы по статусу "EXECUTED"

Пользователь: test

Программа: Статус операции "test" недоступен.

Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

# После фильтрации программа выводит следующие вопросы для уточнения выборки операций,
# необходимых пользователю, и выводит в консоль операции, соответствующие выборке пользователя:

Программа: Отсортировать операции по дате? Да/Нет

Пользователь: да

Программа: Отсортировать по возрастанию или по убыванию? 

Пользователь: по возрастанию/по убыванию

Программа: Выводить только рублевые транзакции? Да/Нет

Пользователь: да

Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

Пользователь: да/нет

Программа: Распечатываю итоговый список транзакций...

Программа: 
Всего банковских операций в выборке: 4

08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD

18.07.2018 Перевод организации 
Visa Platinum 7492 65** **** 7202 -> Счет **0034
Сумма: 8390 руб.

03.06.2018 Перевод со счета на счет
Счет **2935 -> Счет **4321
Сумма: 8200 EUR

# Если выборка оказалась пустой, программа выводит сообщение:

Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации
```

## Документация

Вы можете выполнить команду pytest в терминале.

Файлы тестирования модулей расположены в папке tests.

Протестированы модули:

    src\
    ├── masks.py
    ├── processing.py
    ├── widget.py
    ├── generators.py
    ├── decorators.py
    ├── external_api.py
    ├── read_csv_xlsx_files.py
    ├── process_bank.py
    └── utils.py

## Лицензия:

Отобрали
