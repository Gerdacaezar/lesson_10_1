import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(example_dict):
    assert filter_by_state(example_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(example_dict):
    assert filter_by_state(example_dict, needs_state="CANCELED") == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},

    ]


@pytest.mark.parametrize(
    "dicts",
    [
        1,
        1.0,
        True,
        None,
    ],
)
def test_filter_by_state_type_error(dicts):
    with pytest.raises(TypeError):
        filter_by_state(dicts)


def test_filter_by_state_empty():
    assert filter_by_state([]) == []


def test_filter_by_state_key_error(example_dict_crashed):
    with pytest.raises(KeyError):
        filter_by_state(example_dict_crashed)



