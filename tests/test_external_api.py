from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_to_rub(mock_get):
    mock_get.return_value.text = '{"result": 81.00}'
    assert convert_to_rub(1, "USD") == 81.00
