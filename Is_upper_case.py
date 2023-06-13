"""
The problem:
    Is the string uppercase
"""



def is_uppercase(string):
    return True if string.upper()[0] == string[0] else False


print(is_uppercase('Cheikh'))
print(is_uppercase('cheikh'))
