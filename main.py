import datetime
import re

from src.generators import filter_by_currency
from src.process_bank import process_bank_search_description
from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx_files import read_csv_file, read_excel_file
from src.utils import read_json_file
from src.widget import mask_account_card


def main() -> None:
    # Задаем переменные
    format_choice = None
    status_choice = None
    sort_by_date_choice = None
    sort_by_order_choice = None
    sort_by_order_choice_bool = True
    currency_filter_choice = None
    word_filter_choice = None
    filter_word: str = type[str]
    all_transactions: list[dict] = []

    # Программа приветствует пользователя
    print()

    print(
        """Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    )

    while format_choice not in [1, 2, 3]:
        try:
            format_choice = int(input("Пользователь: "))
        except ValueError:
            pass
        print()
        if format_choice not in [1, 2, 3]:
            print("Программа: Для обработки выбран неверный формат файла.")

    if format_choice == 1:
        print("Программа: Для обработки выбран JSON-файл.")
    elif format_choice == 2:
        print("Программа: Для обработки выбран CSV-файл.")
    elif format_choice == 3:
        print("Программа: Для обработки выбран XLSX-файл.")
    print()

    # После пользователь выбирает статус интересующих его операций
    print(
        """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
    )
    while status_choice not in ["EXECUTED", "CANCELED", "PENDING"]:
        try:
            status_choice = input("Пользователь: ").upper()
        except ValueError:
            pass
        print()

    if status_choice not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Программа: Статус операции "{status_choice}" недоступен.')
    else:
        print(f'Программа: Операции отфильтрованы по статусу "{status_choice}"')
    print()

    #  После фильтрации программа выводит следующие вопросы для уточнения выборки операций,
    #  необходимых пользователю, и выводит в консоль операции, соответствующие выборке пользователя:

    # Сортировка по дате
    print("Программа: Отсортировать операции по дате? Да/Нет")
    print()
    while sort_by_date_choice not in ["да", "нет"]:
        try:
            sort_by_date_choice = input("Пользователь: ").lower()
        except ValueError:
            pass
        print()

    if sort_by_date_choice not in ["да", "нет"]:
        print(f'Программа: сортировка по "{sort_by_date_choice}" недоступна.')
        print()

    # Порядок сортировки
    print("Программа: Отсортировать по возрастанию или по убыванию? ")
    print()
    while sort_by_order_choice not in ["по возрастанию", "по убыванию"]:
        try:
            sort_by_order_choice = input("Пользователь: ").lower()
            if sort_by_order_choice == "по возрастанию":
                sort_by_order_choice_bool = False
        except ValueError:
            pass
        print()

    if sort_by_order_choice not in ["по возрастанию", "по убыванию"]:
        print(f'Программа: сортировка по "{sort_by_order_choice}" недоступна.')
        print()

    # Фильтрация по валюте
    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    print()
    while currency_filter_choice not in ["да", "нет"]:
        try:
            currency_filter_choice = input("Пользователь: ").lower()
        except ValueError:
            pass
        print()

    if currency_filter_choice not in ["да", "нет"]:
        print(f'Программа: фильтрация по "{currency_filter_choice}" недоступна.')
        print()

    # Фильтрация по определенному слову
    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    print()
    while word_filter_choice not in ["да", "нет"]:
        try:
            word_filter_choice = input("Пользователь: ").lower()
        except ValueError:
            pass
        print()

    if word_filter_choice not in ["да", "нет"]:
        print(f'Программа: фильтрация по "{word_filter_choice}" недоступна.')
        print()
    if word_filter_choice == "да":
        try:
            print("Программа: введите слово-фильтр")
            filter_word: re.Match[str] = input("Пользователь: ")
        except ValueError:
            pass
        print()

    # После сбора основной информации начинаем собирать желаемый результат
    print("Программа: Распечатываю итоговый список транзакций...")
    print()

    # Первым делом достаем из файла список словарей со всеми транзакциями
    if format_choice == 1:
        all_transactions = read_json_file("data/operations.json")
    elif format_choice == 2:
        all_transactions = read_csv_file("data/transactions.csv")
    elif format_choice == 3:
        all_transactions = read_excel_file("data/transactions_excel.xlsx")

    # Далее фильтруем список словарей по статусу
    filter_status_operations = filter_by_state(all_transactions, status_choice)

    # Сортируем по дате и по порядку
    if sort_by_date_choice == "да":
        filer_status_sort_by_date_operations = sort_by_date(filter_status_operations, sort_by_order_choice_bool)
    else:
        filer_status_sort_by_date_operations = filter_status_operations

    # Фильтруем по валюте
    if currency_filter_choice == "да":
        filter_status_currency_sort_by_date_operations = list(
            filter_by_currency(filer_status_sort_by_date_operations, "RUB")
        )
    else:
        filter_status_currency_sort_by_date_operations = filer_status_sort_by_date_operations

    # Фильтруем по слову
    if word_filter_choice == "да":
        result = process_bank_search_description(filter_status_currency_sort_by_date_operations, filter_word)
    else:
        result = filter_status_currency_sort_by_date_operations

    # Теперь делаем вывод информации в консоль

    # Если список пуст
    if len(result) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(
            f"""Программа:
    Всего банковских операций в выборке: {len(result)}"""
        )
        print()

        # В каждом сообщении несколько строк
        for operation in result:
            correct_date = ""
            # Первая строка
            if len(operation["date"]) == 26:
                date = datetime.datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
                correct_date = date.strftime("%d.%m.%Y")
            elif len(operation["date"]) == 20:
                date = datetime.datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%SZ")
                correct_date = date.strftime("%d.%m.%Y")
            print(f'{correct_date} {operation["description"]}')

            # Вторая строка
            correct_to = mask_account_card(operation["to"])
            if operation["description"] != "Открытие вклада":
                correct_from = mask_account_card(operation["from"])
                print(f"{correct_from} -> {correct_to}")
            else:
                print(correct_to)

            # Третья строка
            if "operationAmount" in operation:
                correct_amount = round(float(operation["operationAmount"]["amount"]))
                correct_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {correct_amount} {correct_name}")
            elif "amount" in operation:
                correct_amount = round(float(operation["amount"]))
                correct_name = operation["currency_name"]
                print(f"Сумма: {correct_amount} {correct_name}")
            print()


if __name__ == "__main__":
    main()
