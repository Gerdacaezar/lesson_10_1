import pytest

from utils.code import up_first, reverse_list, reverse_string


def test_up_first():
    assert up_first("skypro") == "Skypro"


def test_up_first_for_empty():
    assert up_first("") == ""


# тест, который придумал я, без фикстур
def test_reverse_list_me():
    assert reverse_list([False, 1, 2, 3, "four", "five"]) == ["five", "four", 3, 2, 1, False]


# этот тоже мой (оказалось что эти тесты придумал не только я, но и преподы)
def test_reverse_list_for_empty_me():
    assert reverse_list([]) == []


# учебный пример (переехал в файл conftest.py)
@pytest.fixture
def my_list():
    return [False, 1, 2, 3, "four", "five"]


def test_reverse_list(my_list):
    assert reverse_list(my_list) == ["five", "four", 3, 2, 1, False]


@pytest.mark.parametrize("string, expected_result", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("12345", "54321"),
    ("", ""),
])
def test_reverse_string(string, expected_result):
    assert reverse_string(string) == expected_result
    