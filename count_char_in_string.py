
"""
The Problem: 
    count an character in string 

"""

def counter (string,char):
    x=0
    for character in string :
        x+=1 if character == char else 0
    return x


print(counter("cchlds", "c")) # => 2