"""
The problem:
    we want to return wich quarter of year the month you entered
"""


def index(month):
    if 1 <= month <= 3:
        return "First"
    if 3 < month < 7:
        return "Second"
    if 7 <= month <= 12:
        return "Third"


print(index(3))
print(index(10))
print(index(5))
