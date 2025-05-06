from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскировки номера карты или аккаунта"""
    if type(type_and_number) != str:
        return "incorrect input. input must be str"
    if len(type_and_number) == 0:
        return "empty input"
    list_type_and_number = type_and_number.split()
    if len(list_type_and_number) < 2:
        return "incorrect input. no type number"
    if not list_type_and_number[-1].isdigit():
        return "incorrect input. number not digit"
    if len(list_type_and_number[-1]) == 16:
        list_type_and_number[-1] = get_mask_card_number(list_type_and_number[-1])
        return " ".join(list_type_and_number)
    elif len(list_type_and_number[-1]) == 20:
        list_type_and_number[-1] = get_mask_account(list_type_and_number[-1])
        return " ".join(list_type_and_number)
    else:
        return "incorrect input. number len != 16 or 20"


def get_date(raw_date: str) -> str:
    """Функция возвращает дату формата ДД.ММ.ГГГГ из технической строки формата ГГГГ-ММ-ДД..."""
    if type(raw_date) != str:
        return "incorrect input. input must be str"
    if len(raw_date) == 0:
        return "empty input"
    list_date = [raw_date[8:10], raw_date[5:7], raw_date[:4]]
    for num in list_date:
        if not num.isdigit():
            return "incorrect input. number not digit"
    return ".".join(list_date)


# for x in [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]:
#     print(get_date(x["date"]))
