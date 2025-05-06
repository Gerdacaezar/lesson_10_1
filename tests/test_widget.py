import pytest


from src.widget import mask_account_card, get_date


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


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_date(number, expected_result):
    assert get_date(number) == expected_result


@pytest.mark.parametrize(
    "number",
    [
        20190703183529512364,
        20180630020858425572,
        20180912212725.241689,
        20181014082133.419441,
        True,
        False,
        None,
        [2019, 7, 3, "T18", 35, 29.512364],
        [2018, "06", 30, "T02", "08", 58.425572],
        ("2018-09-12T21", "27:25.241689"),
        (2018, "10-14T08:21:33", 419441),
        {"2019-07-03": "T18:35:29.512364"},
        {20180630: "T02:08:58.425572"},
    ],
)
def test_get_date_not_str(number, input_not_str):
    assert get_date(number) == input_not_str


@pytest.mark.parametrize(
    "number",
    [
        "T2019-07-03T18:35:29.512364",
        "018-06-30T02:08:58.425572",
        "2018-T9-12T21:27:25.241689",
        "2018-10-P4T08:21:33.419441",
    ],
)
def test_get_date_not_digit(number, input_not_digit):
    assert get_date(number) == input_not_digit


def test_get_date_empty():
    assert get_date("") == "empty input"
