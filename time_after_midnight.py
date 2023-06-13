"""
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
The problem:
    the clock shows h : hours after midnight , m : minutes after midnight , s: seconds after midnight
    create an function which return the time since midnight in milliseconds
"""


def time(hours : int , minutes : int, secondes : int ):
    
    return hours * 3600000 + minutes * 60000 + secondes *  1000 


print(time(0, 1, 1))