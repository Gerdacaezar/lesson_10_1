# import logging
#
# name = "Alice"
# age = 30
#
# print(f"Имя: {name}, возраст: {age}")
#
# logging.basicConfig(level=logging.DEBUG)
#
# logging.info(f"Имя: {name}, возраст: {age}")
#
# logging.debug("Это сообщение уровня DEBUG")
# logging.info("Это сообщение уровня INFO")
# logging.warning("Это сообщение уровня WARNING")
# logging.error("Это сообщение уровня ERROR")
# logging.critical("Это сообщение уровня CRITICAL")

# # Импортируем модуль logging
# import logging
#
# # Получаем корневой логер
# logger = logging.getLogger()
#
# # Логируем сообщение уровня ERROR
# logger.error("Это ошибка")
#
# # Получаем логер с определенным именем
# named_logger = logging.getLogger("mylogger")
#
# # Логируем сообщение уровня CRITICAL
# named_logger.critical("Очень критично")

# import logging
#
# # Получение корневого логера
# root_logger = logging.getLogger()
#
# # Создание и получение именованного логера
# app_logger = logging.getLogger("my_application")

# # Подключаем модуль logging
# import logging
#
# # Создаем логер с именем текущего модуля __name__
# logger = logging.getLogger(__name__)
# # Создаем обработчик, который будет выводить лог-сообщения в консоль
# console_handler = logging.StreamHandler()
# # Добавляем обработчик к логеру. Это означает, что все сообщения, отправленные логеру,
# # будут обрабатываться этим обработчиком и выводиться в консоль
# logger.addHandler(console_handler)
# # Устанавливаем уровень логирования для логера на DEBUG.
# # Логер будет обрабатывать все сообщения уровня DEBUG и выше (INFO, WARNING, ERROR, CRITICAL)
# logger.setLevel(logging.DEBUG)
# # Отправляем сообщение уровня DEBUG — 'Debug message'.
# # Поскольку уровень логера установлен на DEBUG, это сообщение будет обработано и выведено в консоль
# logger.debug('Debug message')

# # Подключаем модуль logging:
# import logging
#
# # Создаем логер с именем текущего модуля __name__:
# logger = logging.getLogger(__name__)
# # Создаем хендлер для вывода лог-сообщений в файл example.log:
# file_handler = logging.FileHandler("example.log")
# # Добавляем хендлер к логеру. Это означает, что все сообщения, отправленные логеру,
# # будут обрабатываться этим хендлером и записываться в файл.
# logger.addHandler(file_handler)
# # Устанавливаем уровень логирования для логера на DEBUG.
# # Логер будет обрабатывать все сообщения уровня DEBUG и выше (INFO, WARNING, ERROR, CRITICAL):
# logger.setLevel(logging.DEBUG)
# # Отправляем сообщение уровня DEBUG — 'Debug message'.
# # Поскольку уровень логирования установлен на DEBUG, это сообщение будет обработано и записано в файл example.log.
# logger.debug("Debug message")

import logging

# Создаем логер с именем модуля __name__
logger = logging.getLogger(__name__)
# Создаем хендлер FileHandler для вывода логов в файл example.log
file_handler = logging.FileHandler("example.log", mode="w")
# Создаем форматер Formatter для форматирования вывода используемого хендлера
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
# Устанавливаем созданный форматер для хендлера
file_handler.setFormatter(file_formatter)
# Добавляем хендлер в логер
logger.addHandler(file_handler)
# Устанавливаем уровень логирования на DEBUG
logger.setLevel(logging.DEBUG)

# Выводим сообщения разных уровней — от DEBUG до CRITICAL
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
