import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


# Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего
# курса валют и конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь
# Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модуль external_api.
# Используйте переменные окружения из файла .env для сокрытия чувствительных данных (токенов доступа для API).
def convert_to_rub(amount: str | int | float, currency: str) -> float | Any:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_KEY}
    params = {
        "amount": amount,
        "from": currency,
        "to": "RUB",
    }
    response = requests.get(url, params=params, headers=headers)
    result = (json.loads(response.text))["result"]
    return result
