"""
The problem :
    we want to remover the reapeated "!" in an string
"""


def remover(string):
    new_string = ""
    for char in string:
        if not char == "!":
            new_string += char
    return new_string


print(remover("Hello!"))
print(remover("H!e!l!l!o"))
print(remover("all! done!"))
