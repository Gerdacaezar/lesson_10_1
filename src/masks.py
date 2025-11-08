import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w", "UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str | int) -> str:
    """Функция, которая маскирует номер карты"""
    try:
        logger.info("Запуск функции get_mask_card_number")
        if type(card_number) not in [str, int]:
            logger.info("Некорректный ввод. Ввод должен быть str | int")
            return "incorrect input. input must be str | int"
        str_card = str(card_number)
        if len(str_card) == 0:
            logger.info("Некорректный ввод. Ввод пустой")
            return "empty input"
        if not str_card.isdigit():
            logger.info("Некорректный ввод. Ввод не числовой")
            return "incorrect input. number not digit"
        if len(str_card) != 16:
            logger.info("Некорректный ввод. Ввод != 16")
            return "incorrect input. len != 16"
        logger.info("Возврат замаскированного номера карты")
        return f"{str_card[0:4]} {str_card[4:6]}** **** {str_card[12:]}"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return ""


def get_mask_account(account_number: str | int) -> str:
    """Функция, которая маскирует номер аккаунта"""
    try:
        logger.info("Запуск функции get_mask_account")
        if type(account_number) not in [str, int]:
            logger.info("Некорректный ввод. Ввод должен быть str | int")
            return "incorrect input. input must be str | int"
        str_account = str(account_number)
        if len(str_account) == 0:
            logger.info("Некорректный ввод. Ввод пустой")
            return "empty input"
        if not str_account.isdigit():
            logger.info("Некорректный ввод. Ввод не числовой")
            return "incorrect input. number not digit"
        if len(str_account) != 20:
            logger.info("Некорректный ввод. Ввод != 20")
            return "incorrect input. len != 20"
        logger.info("Возврат замаскированного номера аккаунта")
        return "**" + str_account[-4:]
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return ""
