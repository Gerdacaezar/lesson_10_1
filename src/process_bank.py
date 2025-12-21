import re
from collections import Counter


def process_bank_search_description(data: list[dict], search: re.Match[str] | None) -> list[dict]:
    """Функция, которая принимает список словарей
    с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    При реализации этой функции используйте библиотеку re для работы с регулярными выражениями."""
    result = []
    pattern = re.compile(str(search))

    for operation in data:
        search = re.search(pattern, operation["description"])
        if search:
            result.append(operation)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая принимает список словарей
    с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description."""
    descriptions = []

    for operation in data:
        if operation["description"] in categories:
            descriptions.append(operation["description"])

    counted = Counter(descriptions)
    return dict(counted)
