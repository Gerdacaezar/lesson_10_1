import os
from dotenv import load_dotenv
import requests
import json


# Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего
# курса валют и конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь
# Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модуль external_api.
# Используйте переменные окружения из файла .env для сокрытия чувствительных данных (токенов доступа для API).
def convert_to_rub(amount: str | int | float, currency: str) -> float:
    load_dotenv()
    api_key = os.getenv('API_KEY')

    # Так как API блокирует любые мои попытки использовать свой функционал, то приходится пользоваться только latest
    url = 'http://api.exchangeratesapi.io/v1/latest'
    params = {'access_key': api_key}
    response = requests.get(url, params=params)

    # Сначала конвертируем искомую валюту в EUR
    rates = (json.loads(response.text))['rates']
    amount_in_eur = float(amount) / rates[currency]

    # Теперь в RUB
    amount_in_rub = amount_in_eur * rates['RUB']
    return amount_in_rub
