import random
import requests


def get_random_number():
    return random.randint(0, 10)


print(get_random_number())


def get_github_user_info(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    return response.json()


print(get_github_user_info('gerdacaezar'))