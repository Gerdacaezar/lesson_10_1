# Задача 1.
# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми,
# и округляет их до целых, если это не так. Декоратор должен принимать параметр precision, который указывает,
# до скольких цифр после запятой округлять числа.

def round_it(precision):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return round(result, precision) if not result % 10 == 0 else result
        return inner
    return wrapper


@round_it(3)
def integer():
    return 2.33333333


print(integer())  # >>> 2.333

# Задача 2.
# Напишите декоратор, который повторно вызывает декорируемую функцию заданное количество раз через заданное время,
# если произошла ошибка. Параметры, передаваемые в декоратор, обязательно должны быть именованными.
import time


def retry(repeat_times, time_of_repeat):
    def wrapper(func):
        def inner(*args, **kwargs):
            for _ in range(repeat_times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ... {e}")
                    time.sleep(time_of_repeat)
            raise Exception(f"Max retries exceeded")
        return inner
    return wrapper


# Задача 3.
# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
# в котором каждое слово сокращено до определенной длины. Если слово было сокращено,
# в конце слова ставится переданный символ.
# Количество символов в слове и знак в конце сокращенного слова — параметры декоратора,
# причем символ обязательно должен передаваться как именованный аргумент.



# Задача 4.
# Напишите тесты с использованием библиотеки pytest для проверки корректности работы декоратора из задачи 3.
