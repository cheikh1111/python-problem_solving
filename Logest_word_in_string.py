"""
The problem find longest word in a string

"""

def longest(str):
    longest=""
    for word in str.split(): longest = word if len(word)>len(longest) else longest
    return longest


print(longest("Python Php Javascript C++ Css"))