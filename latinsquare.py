"""
A latin square is an n × n array filled with the integers 1 to n, each occurring once in each row and column.

"""
from random import shuffle


def square(num):
    latin_square = [[numm for numm in range(num)] for number in range(num)]
    shuffle(latin_square)
    for squaree in latin_square:
        shuffle(squaree)
    return latin_square


print(square(4))
