from functools import reduce
from typing import TypeVar


def poo(x):
    if isinstance(x, list):
        return reduce(TypeVar.__or__, map(poo, x))
    return TypeVar(repr(x))


def pee(xs):
    return [*map(lambda x: int(x.__name__), xs.__args__)]


xs = [1, [2, 3], [[4], 5, [6, [7, [8]]]]]
print(pee(poo(xs)))

# output:
# [1, 2, 3, 4, 5, 6, 7, 8]
