"""
The Problem :
    remove  first and last character in a string

"""


def remove(string) -> str:

    new_string=""
    for i in range(1,len(string)-1):
        new_string += string[i]

    return new_string

print(remove('cheikh'))
