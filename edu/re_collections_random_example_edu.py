import json
import re
from collections import Counter


# Дан файл access.log, содержащий большой объем текста и email-адресов.
# Необходимо с помощью регулярных выражений «вытащить» оттуда все email-адреса,
# подсчитать количество вхождений каждого домена почтового сервиса и сохранить результат в JSON-файле result.json.
# Для решения задачи необходимо использовать библиотеки re, json и collections.
def count_emails(input_file: str, output_file: str):
    # Открываем файл
    with open(input_file) as access_file:
        data_from_file = access_file.read()

    # Находим все email`ы
    pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
    email_list = re.findall(pattern, data_from_file)

    # Вытаскиваем из email`ов все домены и подсчитываем
    domains = Counter(item.split("@")[1] for item in email_list)
    result = {"total_count": len(email_list), "domains": {}}
    for domain, count in domains.items():
        domain_emails = [email for email in email_list if email.split("@")[1] == domain]
        result["domains"][domain] = {"count": count, "emails": domain_emails}

    with open(output_file, "w", encoding="utf-8") as of:
        json.dump(result, of, indent=4)


print(count_emails("../data/access.log", "result.json"))
