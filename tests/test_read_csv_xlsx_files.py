from unittest.mock import mock_open, patch

import pandas as pd

from src.read_csv_xlsx_files import read_csv_file, read_excel_file


@patch("builtins.open", new_callable=mock_open)
@patch("csv.DictReader")
def test_read_csv_file(mock_dict_reader, mock_file):
    mock_dict_reader.return_value = [
        {"name": "Иван", "age": "25", "city": "Москва"},
        {"name": "Мария", "age": "30", "city": "СПб"},
    ]
    result = read_csv_file("example.csv")
    mock_file.assert_called_once_with("example.csv", "r", encoding="utf-8")
    mock_dict_reader.assert_called_once()
    expected = [{"name": "Иван", "age": "25", "city": "Москва"}, {"name": "Мария", "age": "30", "city": "СПб"}]
    assert expected == result


@patch("pandas.read_excel")
def test_read_excel_file(mock_read_excel):
    mock_df = pd.DataFrame(
        [{"name": "Иван", "age": "25", "city": "Москва"}, {"name": "Мария", "age": "30", "city": "СПб"}]
    )
    mock_read_excel.return_value = mock_df
    result = read_excel_file("example.xlsx")
    mock_read_excel.assert_called_once()
    expected = [{"name": "Иван", "age": "25", "city": "Москва"}, {"name": "Мария", "age": "30", "city": "СПб"}]
    assert expected == result
