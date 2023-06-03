"""

The problem is find if the year is leap

"""


def is_leap(year):
    return True if year%4 == 0 else False


print(is_leap(2000))
print(is_leap(1999))