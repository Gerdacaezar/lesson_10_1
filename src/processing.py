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


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        sort_range=False,
    )
)

# print(sort_by_date(1))


# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#     )
# )
