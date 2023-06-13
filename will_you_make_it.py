
"""
Problem:
    1. I have only two galons of fuel left
    2. nearest pump is 50 miles away
    3. my car can run about 25 miles per galon

    Create an function to calculate if you will make it or not

"""


def will_you_make_it(left_fuel , space_before_pump , space_per_gallon):

    return True if left_fuel * space_per_gallon == space_before_pump else False


print(will_you_make_it(2, 50 , 25 ))
