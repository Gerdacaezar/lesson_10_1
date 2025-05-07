def filter_by_state(list_of_id: list[dict], needs_state: str = "EXECUTED") -> list[dict] | None:
    """Функция фильтрации списка ID по 'state' (по умолчанию needs_state = 'EXECUTED')"""
    result = []
    for id_dict in list_of_id:
        if id_dict["state"] == needs_state:
            result.append(id_dict)
    return result


def sort_by_date(list_of_id: list[dict], sort_range: bool = True) -> list[dict] | None:
    """Функция сортировки списка ID по 'date' (по умолчанию (sort_range = True) по убыванию)"""
    return sorted(list_of_id, key=lambda x: x["date"], reverse=sort_range)
