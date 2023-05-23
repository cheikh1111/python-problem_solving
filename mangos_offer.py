"""
The problem:
    count the price of mango ,with today ofter that consiste to have one free mango for every three mangos
"""


def count(mangos):
    mango_price = 300
    for x in range(int(mangos / 3)):
        mangos + 1
    return mangos * mango_price


print(count(3))
