# Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10.
print(*(x**3 for x in range(11) if x % 2 == 0))
# >>> 0 8 64 216 512 1000


# Напишите функцию, которая принимает список чисел
# и возвращает сумму квадратов положительных чисел в этом списке.
# Используйте для этого генераторное выражение.
def sum_of_squares(num_list: list[int]) -> int:
    return sum(x * x for x in num_list if x > 0)


print(sum_of_squares([-2, -1, 0, 1, 2, 3, 4]))
# >>> 30

# Напишите генераторное выражение, которое возвращает буквы строки "hello", но только если они являются гласными.
print(*(x for x in "hello" if x in ["a", "e", "i", "o", "u"]))

# Найдите среднее арифметическое всех чисел, кратных 3 или 5, в диапазоне от 1 до 100 включительно.

range_list = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
print(sum(range_list) / len(range_list))


# Объедините несколько списков в один список, учитывая возможные дубликаты элементов.
def union_list(*lists: list) -> list:
    result: set = set()
    for lst in lists:
        result = result.union(set(lst))
    return list(result)


print(union_list([1, 2, 3], [2, 3, 4], [4, 5, 6]))

# Дан список словарей. Отфильтруйте его по ключу age и значению 30.
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

print([x for x in people if x["age"] == 30])
