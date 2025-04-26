from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскировки номера карты или аккаунта"""
    list_type_and_number = type_and_number.split()
    if len(list_type_and_number[-1]) == 16:
        list_type_and_number[-1] = get_mask_card_number(list_type_and_number[-1])
    else:
        list_type_and_number[-1] = get_mask_account(list_type_and_number[-1])
    return " ".join(list_type_and_number)
