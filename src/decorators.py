# Напишите декоратор log, который будет автоматически логировать начало и конец выполнения функции,
# а также ее результаты или возникшие ошибки.

# Декоратор должен принимать необязательный аргумент filename, который определяет,
# куда будут записываться логи (в файл или в консоль):
#         Если filename задан, логи записываются в указанный файл.
#         Если filename не задан, логи выводятся в консоль.

# Логирование должно включать:
#         Имя функции и результат выполнения при успешной операции.
#         Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable[[Callable], Callable]:
    def wrapper(func: Callable) -> Callable:
        """Декоратор @log() для логирования результатов выполнения функции.
        Если не задавать параметр, то логи выведутся в консоль.
        Впишите в декоратор параметр @log(filename="log.txt") и результат запишется в файл log.txt
        """

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_text = f"{func.__name__} ok"
                if filename:
                    with open(filename, "w") as file:
                        file.write(log_text)
                else:
                    print(log_text)
                return result
            except Exception as e:
                log_text = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w") as file:
                        file.write(log_text)
                else:
                    print(log_text)
                raise e

        return inner

    return wrapper
