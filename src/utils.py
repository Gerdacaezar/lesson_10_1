import json
import logging
from typing import Any

from src.external_api import convert_to_rub

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w", "UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


# Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
# о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
# Функцию поместите в модуль utils.
# Файл с данными о финансовых транзакциях operations.json поместите в директорию data/ в корне проекта.
def read_json_file(file: str) -> list[dict] | Any:
    """
    Функция принимает на вход путь до json-файла и возвращает содержимое в виде списка словарей
    Если json-файл пустой, содержит не список или не найден, функция возвращает пустой список
    """
    try:
        logger.info("Открытие JSON-файла")
        with open(file, "r", encoding="UTF-8") as f:
            logger.info("Возврат списка словарей")
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


# Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
# тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего
# курса валют и конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь
# Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
def rub_amount(transaction: dict) -> float | Any:
    """
    Функция принимает на вход транзакцию в виде словаря и возвращает сумму транзакции в рублях.
    Если транзакция была произведена не в рублях, то происходит обращение к функции конвертации в рубли convert_to_rub
    из src/external_api.py.
    """
    try:
        logger.info("Извлечение значения из словаря")
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("Извлечение значения из словаря если оно в рублях")
            amount = transaction["operationAmount"]["amount"]
            return amount
        else:
            logger.info("Извлечение значения из словаря если оно не в рублях")
            amount = convert_to_rub(
                transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
            )
            return amount
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return 0.0


# Функцию конвертации поместите в модуль external_api.
# Создайте шаблон файла .env и разместите в репозитории на GitHub.
# Напишите тесты для новых функций, используйте Mock и patch.
