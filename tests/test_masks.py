import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected_card_num",
    [
        (1596837868705199, "1596 83** **** 5199"),
        (7158300734726758, "7158 30** **** 6758"),
        (6831982476737658, "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
        ("1234123412341234", "1234 12** **** 1234")
    ]
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
        {71583007: "34726758"}
    ]
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
        "aaaaaaaaaaaaaaaa"
    ]
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
        "715830073472675834726758"
    ]
)
def test_get_mask_card_number_not_16(card_num, input_not_16):
    assert get_mask_card_number(card_num) == input_not_16


@pytest.mark.parametrize(
    "card_num",
    [
        "",
        ''
    ]
)
def test_get_mask_card_number_empty(card_num, empty_input):
    assert get_mask_card_number(card_num) == empty_input
