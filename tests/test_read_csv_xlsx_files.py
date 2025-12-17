from src.read_csv_xlsx_files import read_csv_file, read_excel_file
import pandas as pd
import pytest
from unittest.mock import Mock, patch


@patch('pandas.read_csv')
def test_read_csv_file(mock_read_csv):
    mock_df = pd.DataFrame(
        {
            'A': [1, 2],
            'B': [3, 4],
        }
    )
    mock_read_csv.return_value = mock_df
    result_df = read_csv_file('example.csv')
    mock_read_csv.assert_called_once_with('example.csv')

    assert read_csv_file('example.csv') == result_df