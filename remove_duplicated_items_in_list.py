"""
The problem:
    We want to create new list from old one an delete duplicated numbers
"""

numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    2,
    5,
    1,
    2,
    5,
    4,
    9,
    7,
    7,
    2,
    3,
    4,
    7,
    8,
    6,
    2,
    3,
    4,
]

# first solution
new_numbers = []
for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
        new_numbers.sort()
print(new_numbers)


# Second Solution
def minify(numbers):
    return list(set(numbers))


print(minify(numbers))
