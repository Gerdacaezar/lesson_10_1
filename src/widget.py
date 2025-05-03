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


for x in [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]:
    print(mask_account_card(x))
