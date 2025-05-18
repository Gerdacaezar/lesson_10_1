from typing import Generator


def filter_by_currency(list_of_transactions: list[dict], currency: str) -> Generator[dict]:
    """Функция фильтрации списка транзакций по валюте операции"""
    for transaction in list_of_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(list_of_transactions: list[dict]) -> Generator[str]:
    """Функция возвращает описание переводов из списка транзакций"""
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:
    """Функция генерирует номер карты в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    for transaction in range(start, end + 1):
        card_num = "0" * (16 - len(str(transaction))) + str(transaction)
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:]}"
