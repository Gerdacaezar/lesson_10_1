import pytest


@pytest.fixture
def input_not_str():
    return "incorrect input. input must be str"


@pytest.fixture
def input_not_str_int():
    return "incorrect input. input must be str | int"


@pytest.fixture
def input_not_digit():
    return "incorrect input. number not digit"


@pytest.fixture
def input_not_16():
    return "incorrect input. len != 16"


@pytest.fixture
def input_not_20():
    return "incorrect input. len != 20"


@pytest.fixture
def input_not_16_or_20():
    return "incorrect input. number len != 16 or 20"


@pytest.fixture
def no_type_number():
    return "incorrect input. no type number"


@pytest.fixture
def example_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def example_dict_another_state_date():
    return [
        {"id": 41428829, "state": "TESTED", "date": "test"},
        {"id": 939719570, "state": "TESTED", "date": "test"},
        {"id": 594226727, "state": "TESTED", "date": "test"},
        {"id": 615064591, "state": "TESTED", "date": "test"},
    ]


@pytest.fixture
def example_dict_crashed():
    return [
        {"id": 41428829, "stat": "EXECUTED", "dat": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "stat": "EXECUTED", "dat": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "stat": "CANCELED", "dat": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "stat": "CANCELED", "dat": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def example_dict_one_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def example_dict_crashed_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (4, 5, 9), (7, 8, 15)])
def test_add(x, y, expected):
    assert x + y == expected


@pytest.fixture
def transactions():
    return [
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
