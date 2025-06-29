import requests


# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.text)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# payload = {'my_key': 'my_value'}
# r = requests.post('https://httpbin.org/post', data=payload)
#
# print(r.text)

# user = "skypro-008"
# url = f"https://api.github.com/users/gerdacaezar/repos"
#
# response = requests.get(url)
#
# repos = response.json()
#
# for repo in repos:
#     if repo["language"] == "Python":
#         print(f"Name: {repo['name']}\nLink: {repo['html_url']}\n")

import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
github_token = os.getenv('GITHUB_TOKEN')

# Создание заголовка с токеном доступа API
headers = {
    'Authorization': f'token {github_token}'
}

# Отправка GET-запроса к API
response = requests.get('https://api.github.com/gerdacaear', headers=headers)

# Обработка ответа
print(response.json())