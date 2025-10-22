from time import time


# Внешняя функция принимает параметр x
def make_multiplier(x):
    # Внутренняя функция использует значение x из внешней функции
    def multiplier(y):
        return x * y

    # Возвращаем внутреннюю функцию
    return multiplier


# Создаем замыкание
double = make_multiplier(2)
print(double(5))  # >>> 10


# Простой декоратор
def timer(func):
    def wrapper(*args, **kwargs):
        print("Starting time working")
        time_1 = time()  # здесь можно что-то свое добавить
        result = func(*args, **kwargs)
        time_2 = time()  # здесь можно что-то свое добавить
        print(f"Time for work: ({time_2 - time_1})")
        return result

    return wrapper


def printing(func):
    def wrapper(*args, **kwargs):
        print(f"function {func} started")
        result = func(*args, **kwargs)
        print(f"function {func} started")
        return result

    return wrapper


@printing
@timer  # Сначала он, потом остальные снизу вверх
def example():
    print(1 + 1 + 2**4)


example()
