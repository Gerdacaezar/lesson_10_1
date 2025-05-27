import time

# Задача 1.
# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми,
# и округляет их до целых, если это не так.


def all_round(func):
    def round_check(*args, **kwargs):
        result = func(*args, **kwargs)
        for i, value in enumerate(result):
            if not value % 10 == 0:
                result[i] = round(value)
        return result

    return round_check


@all_round
def num_list():
    return [1, 2.4, 3, 4.74, 5.14, 0.06, 2.47, 8, 9]


print(num_list())


# Задача 2.
# Напишите декоратор, который повторно вызывает декорируемую функцию три раза.
# Каждый раз через три секунды, если произошла ошибка.
def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                print("exception")
                time.sleep(3)
        raise Exception("Function call failed after multiple retries.")

    return wrapper


@retry
def excpt():
    raise Exception


print(excpt())


# Задача 3.
# Напишите декоратор, который позволяет возвращать элементы декорируемой функции по одному через yield,
# если эта функция возвращает список или кортеж.
def differ(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) in [list, tuple]:
            for item in result:
                yield item
        else:
            yield result

    return wrapper


@differ
def num_list_2():
    return [1, 2.4, 3, 4.74, 5.14, 0.06, 2.47, 8, 9]


function = num_list_2()
print(next(function))
print(next(function))
print(next(function))


# Задача 4.
# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
# в котором каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка.


# Задача 5.
# Напишите три декоратора, которые можно применять последовательно к результату декорируемой функции.

# Первый декоратор должен заменять в тексте, который выдает функция, все восклицательные знаки "!" на "!!!".

# Второй декоратор должен заменять в тексте, который выдает функция, все знаки вопроса "?" на "???".

# Третий декоратор должен заменять в тексте, который выдает функция, все точки "." на "..."
