from src.utils import read_json_file, rub_amount
from unittest.mock import Mock


def test_read_json_file():
    expected_data = [
        {
            "one": 1,
            "two": 2,
            "three": 3,
            "fours": [4, 4.0, "four", {"four": 4}]
        }
    ]
    assert read_json_file('data/test_json_file.json') == expected_data
    assert read_json_file('data/test_crash_json_file.json') == []
    assert read_json_file('data/test_json_file') == []


def test_rub_amount():
    mock_amount = Mock(return_value=80.0)
