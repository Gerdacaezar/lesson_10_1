result = [x for num in range(20) for x in [num, num] if num % 2 == 0]
print(result)
# >>> [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18]

squares = [x * x for x in [1, 2, 3]]
print(squares)
# >>> [1, 4, 9]

ascii_codes = [ord(c) for c in "Hello!" if c.isalpha() and c.islower()]
print(ascii_codes)
# >>> [101, 108, 108, 111]

matching_indices = [i for i, (x, y) in enumerate([(1, 2), (4, 4), (5, 7), (0, 0)]) if x == y]
print(matching_indices)
# >>> [1, 3]

result = [x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0]
print(result)
# >>> [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30]

print([x * x for x in range(10)])
# >>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def print6(xs: iter) -> any:
    for i, x in enumerate(xs):
        print(x, end=' ')
        if i == 5:
            break


i = (x * x for x in range(10))
print6(i)  #  вызываем функцию для вывода 6 элементов
# >>> 0 1 4 9 16 25

print()
print6(i)  #  продолжаем перебор с точки остановки
# >>> 36 49 64 81

print()
print6(i)
# >>>   # ничего нет, потому что счетчик закончился


num_list = (x for x in range(3))
print(next(num_list))
# >>> 0

print(next(num_list))
# >>> 1

print(next(num_list))
# >>> 2

print(next(num_list, 'тут должна быть ошибка StopIteration, так как счетчик закончился, но она фиксится так'))
# >>> тут должна быть ошибка StopIteration, так как счетчик закончился, но она фиксится так

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*nums)
# >>> 1 2 3 4 5 6 7 8 9

print(*(x for x in "Hello World!" if x.isupper()))
# >>> H W
