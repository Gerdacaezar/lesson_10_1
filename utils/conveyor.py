from itertools import chain


def is_even(x):
    return x % 2 == 0


def dup(x):
    return [x, x]


result_filter = list(filter(is_even, range(20)))

result_map = list(map(dup, result_filter))

result_chain = list(chain(*result_map))

print(result_chain)

