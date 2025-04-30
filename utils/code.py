def up_first(msg: str) -> str:
    """Делает первую букву строки заглавной."""
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


def reverse_list(lst: list) -> list:
    """Функция принимает список и возвращает его в обратном порядке"""
    return lst[::-1]
