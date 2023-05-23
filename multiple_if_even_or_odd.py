"""
The problem :
if the number is even we will multiple it by eight 
else we will multiple it by nine
"""


def multiple(number=0):
    if not number:
        raise ValueError("Please enter an valid number")
    return number * 8 if number % 2 == 0 else number * 9


print(multiple(2))
print(multiple(3))
print(multiple())
