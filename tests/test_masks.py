import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_num, expected_card_num",
    [
        (1596837868705199, "1596 83** **** 5199"),
        (7158300734726758, "7158 30** **** 6758"),
        (6831982476737658, "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
        ("1234123412341234", "1234 12** **** 1234"),
    ],
)
def test_get_mask_card_number(card_num, expected_card_num):
    assert get_mask_card_number(card_num) == expected_card_num


@pytest.mark.parametrize(
    "card_num",
    [
        1596837868705199.0,
        7158300734726758.0,
        True,
        False,
        None,
        [6831982476737658],
        [8990922113665229],
        (59994142, 28426353),
        (12341234, 12341234),
        {"15968378": 68705199},
        {71583007: "34726758"},
    ],
)
def test_get_mask_card_number_not_str_int(card_num, input_not_str_int):
    assert get_mask_card_number(card_num) == input_not_str_int


@pytest.mark.parametrize(
    "card_num",
    [
        "-!9683786870&199",
        "715.300ry4726758",
        "68319kfb76737-58",
        "893cvb 113*`5229",
        "599941#^28426353",
        "12sldgjlwo^7(8-4",
        "qwer:bmnlrmhg199",
        "aaaaaaaaaaaaaaaa",
    ],
)
def test_get_mask_card_number_not_digit(card_num, input_not_digit):
    assert get_mask_card_number(card_num) == input_not_digit


@pytest.mark.parametrize(
    "card_num",
    [
        15968378,
        71583007,
        "68319824",
        "89909221",
        599941422842635328426353,
        123412341234123412341234,
        "159683786870519968705199",
        "715830073472675834726758",
    ],
)
def test_get_mask_card_number_not_16(card_num, input_not_16):
    assert get_mask_card_number(card_num) == input_not_16


@pytest.mark.parametrize("card_num", ["", " "])
def test_get_mask_card_number_empty(card_num, empty_input):
    assert get_mask_card_number(card_num) == empty_input


@pytest.mark.parametrize(
    "account_num, expected_account_num",
    [
        (64686473678894779589, "**9589"),
        (35383033474447895560, "**5560"),
        (73654108430135874305, "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_num, expected_account_num):
    assert get_mask_account(account_num) == expected_account_num


@pytest.mark.parametrize(
    "account_num",
    [
        64686473678894779589.0,
        35383033474447895560.0,
        True,
        False,
        None,
        [73654108430135874305],
        [64686473678894779589],
        (3538303347, 4447895560),
        (73654108430, 135874305),
        {"64686473678": 894779589},
        {35383033474: "447895560"},
    ],
)
def test_get_mask_account_not_str_int(account_num, input_not_str_int):
    assert get_mask_account(account_num) == input_not_str_int


@pytest.mark.parametrize(
    "account_num",
    [
        "72j6-!9683786870&199",
        "98ds715.300ry4726758",
        "tr3668319kfb76737-58",
        "!!-j893cvb 113*`5229",
        "--y8599941#^28426353",
        "=(a312sldgjlwo^7(8-4",
        "l5A2qwer:bmnlrmhg199",
        "aaaaaaaaaaaaaaaaaaaa",
    ],
)
def test_get_mask_account_not_digit(account_num, input_not_digit):
    assert get_mask_account(account_num) == input_not_digit


@pytest.mark.parametrize(
    "account_num",
    [
        6468647367,
        3538303347,
        "7365410843",
        "6468647367",
        353830334744478955604447895560,
        736541084301358743050135874305,
        "646864736788947795898894779589",
        "353830334744478955604447895560",
    ],
)
def test_get_mask_account_not_16(account_num, input_not_20):
    assert get_mask_account(account_num) == input_not_20


@pytest.mark.parametrize("account_num", ["", " "])
def test_get_mask_account_empty(account_num, empty_input):
    assert get_mask_account(account_num) == empty_input
