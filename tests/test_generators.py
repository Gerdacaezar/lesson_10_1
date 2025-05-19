import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_transactions) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_filter_by_currency_another_currency(transactions):
    transaction = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(transaction)


def test_filter_by_currency_empty_transactions(transactions):
    transaction = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(transaction)


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_one_transaction():
    descriptions = transaction_descriptions(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ]
    )
    assert next(descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_empty_transactions():
    descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator():
    card_number = card_number_generator(1, 5)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(card_number)


def test_card_number_generator_max_value():
    card_number = card_number_generator(9999999999999995, 9999999999999999)
    assert next(card_number) == "9999 9999 9999 9995"
    assert next(card_number) == "9999 9999 9999 9996"
    assert next(card_number) == "9999 9999 9999 9997"
    assert next(card_number) == "9999 9999 9999 9998"
    assert next(card_number) == "9999 9999 9999 9999"
    with pytest.raises(StopIteration):
        next(card_number)
