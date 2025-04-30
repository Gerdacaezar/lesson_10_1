import pytest


@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (4, 5, 9), (7, 8, 15)])
def test_add(x, y, expected):
    assert x + y == expected
