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
