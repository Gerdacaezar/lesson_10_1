def get_mask_card_number(card_number: str | int) -> str:
    """Функция, которая маскирует номер карты"""
    if type(card_number) not in [str, int]:
        return "incorrect input. input must be str | int"
    str_card = str(card_number)
    if len(str_card) == 0:
        return "empty input"
    if not str_card.isdigit():
        return "incorrect input. number not digit"
    if len(str_card) != 16:
        return "incorrect input. len != 16"
    return f"{str_card[0:4]} {str_card[4:6]}** **** {str_card[12:]}"


def get_mask_account(account_number: str | int) -> str:
    """Функция, которая маскирует номер аккаунта"""
    if type(account_number) not in [str, int]:
        return "incorrect input. input must be str | int"
    str_account = str(account_number)
    if len(str_account) == 0:
        return "empty input"
    if not str_account.isdigit():
        return "incorrect input. number not digit"
    if len(str_account) != 20:
        return "incorrect input. len != 20"
    return "**" + str_account[-4:]
