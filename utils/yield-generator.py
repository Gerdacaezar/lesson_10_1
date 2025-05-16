from typing import Any, Generator


def simple_generator() -> Any:
    yield 1
    yield 2


gen = simple_generator()

print(next(gen))
# >>> 1
print(next(gen))
# >>> 2
# print(next(gen))
# >>> StopIteration
print(iter(simple_generator()))
# >>> <generator object simple_generator at 0x000002C903F05DD0>
print(simple_generator())
# >>> <generator object simple_generator at 0x000002C903F05DD0>
for value in simple_generator():
    print(value)
# >>> 1
# >>> 2
print("\n" + ">--------------<" + "\n")  # >--------------<


# Задача: Написать генератор бесконечной последовательности чисел
def inf_seq(start: int = 1) -> Generator[int]:
    while True:
        yield start
        start += 1


numbers = inf_seq()
start_3 = inf_seq(3)

print(next(numbers))
# >>> 1
print(next(numbers))
# >>> 2
print(next(numbers))
# >>> 3
print(next(numbers))
# >>> 4
print(next(numbers))
# >>> 5
print(next(start_3), "here")
# >>> 3 here
print(next(start_3), "here")
# >>> 4 here
print("\n" + ">--------------<" + "\n")  # >--------------<


def iterate(x0: int | float, m: int | float) -> Generator[int | float]:
    x: int | float = x0
    while True:
        yield x
        x *= m


for x in iterate(1, 1.2):
    print(x)
    if x > 2:
        break
# >>> 1.2
#     1.44
#     1.728
#     2.0736


def f() -> Generator[str]:
    print("Initializing...")
    yield "one"
    print("Continue...")
    yield "two"
    print("Stopping...")


i = f()
print(next(i))
# >>> Initializing...
#     one
print(next(i))
# >>> Continue...
#     two
# print(next(i))
# >>> Stopping...
#     StopIteration
print("\n" + ">--------------<" + "\n")  # >--------------<

squares = (x * x for x in range(10) if x % 2 == 0)

# Задача 1.
# Напишите генератор, который принимает на вход последовательность чисел и генерирует квадраты этих чисел.


# Задача 2.
# Напишите генератор, который генерирует случайные числа в заданном диапазоне.


# Задача 3.
# Напишите генератор, который генерирует последовательность чисел по заданной формуле.


# Задача 4.
# Напишите генератор, который принимает на вход два списка и генерирует элементы, которые есть в обоих списках.


# Задача 5.
# Напишите тесты на pytest для генератора из задания 4. Тестами покройте граничные случаи.


# * Задача 6.
# Напишите генератор, который принимает на вход размерность квадратной матрицы и генерирует числа по спирали,
# начиная с центрального элемента.
