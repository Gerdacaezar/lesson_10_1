def filter_by_state(list_of_id: list[dict], needs_state: str = 'EXECUTED') -> list[dict] | None:
    result = []
    for id_dict in list_of_id:
         if id_dict['state'] == needs_state:
             result.append(id_dict)
    return result
