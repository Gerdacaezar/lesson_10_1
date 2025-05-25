def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Начало работы")
        func(*args, **kwargs)
        print("Конец работы")
    return wrapper


@my_decorator
def say_hello():
    print(f"hello!")


say_hello()
