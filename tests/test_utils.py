from src.utils import read_json_file, rub_amount


def test_read_json_file():
    expected_data = [{"one": 1, "two": 2, "three": 3, "fours": [4, 4.0, "four", {"four": 4}]}]
    assert read_json_file("data/test_json_file.json") == expected_data
    assert read_json_file("data/test_crash_json_file.json") == []
    assert read_json_file("data/test_json_file") == []


def test_rub_amount_rub():
    expected_data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert rub_amount(expected_data) == "31957.58"
