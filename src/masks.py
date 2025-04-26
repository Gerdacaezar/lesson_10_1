def get_mask_card_number(card_number: str | int) -> str:
    """Функция, которая маскирует номер карты"""
    str_card = str(card_number)
    return f"{str_card[0:4]} {str_card[4:6]}** **** {str_card[12:]}"


def get_mask_account(account_number: str | int) -> str:
    """Функция, которая маскирует номер аккаунта"""
    return "**" + str(account_number)[-4:]
