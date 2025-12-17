import csv

import pandas as pd
from mypy.types import Any


def read_csv_file(path: str) -> list[dict] | Any:
    """Функция преобразования csv-файла в список словарей"""
    data = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def read_excel_file(path: str) -> list[dict] | Any:
    """Функция преобразования excel-файла в список словарей"""
    reader = pd.read_excel(path, sheet_name=0)
    data = reader.to_dict("records")
    return data
