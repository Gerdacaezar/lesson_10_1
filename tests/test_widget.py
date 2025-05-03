import pytest


from src.widget import mask_account_card


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(number, expected_result):
    assert mask_account_card(number) == expected_result


@pytest.mark.parametrize(
    "number",
    [
        73654108430135874305,
        5999414228426353,
        1596837868705199.0,
        64686473678894779589.0,
        True,
        False,
        None,
        ["MasterCard", 7158300734726758],
        ["Счет", "35383033474447895560"],
        ("Visa Classic", 6831982476737658),
        ("Visa Platinum", "8990922113665229"),
        {"Visa Gold": 5999414228426353},
        {"Счет": "73654108430135874305"},
    ],
)
def test_mask_account_card_not_str(number, input_not_str):
    assert mask_account_card(number) == input_not_str


@pytest.mark.parametrize(
    "number",
    [
        "Maestro Maestro",
        "Счет Счет",
        "MasterCard 7158300qaw726758",
        "Счет 3538303-47!4ty895560",
        "Visa Classic 68319op476737=_8",
        "Visa Platinum g99092/113665229",
        "Visa Gold Gold5999414228426353",
        "Счет Счет73654108430135874305",
    ],
)
def test_mask_account_card_not_digit(number, input_not_digit):
    assert mask_account_card(number) == input_not_digit


@pytest.mark.parametrize(
    "number",
    [
        "Maestro 15968378",
        "Счет 6468647367",
        "MasterCard 715830073472675834726758",
        "Счет 353830334744478955604447895560",
    ],
)
def test_mask_account_card_not_16_or_20(number, input_not_16_or_20):
    assert mask_account_card(number) == input_not_16_or_20


@pytest.mark.parametrize(
    "number",
    [
        "Maestro",
        "Счет",
        "715830073472675834726758",
        "353830334744478955604447895560",
    ],
)
def test_mask_account_card_no_type_number(number, no_type_number):
    assert mask_account_card(number) == no_type_number


def test_get_mask_account_card_empty():
    assert mask_account_card("") == "empty input"
