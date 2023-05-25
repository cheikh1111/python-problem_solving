"""
The problem:
    we want to return maximum and minimum value in list
"""


def min_max(list):
    return "Min : " + str(min(list)) + "  " + "Max : " + str(max(list))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


print(min_max(my_list))
