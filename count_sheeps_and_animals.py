"""
https://www.codewars.com/kata/54edbc7200b811e956000556
The Problem:
    Consider an array/list of sheep where some sheep may be missing from their place.
     We need a function that counts the number of sheep present in the array (True means present).

"""



def count(array):
    sheep = null_or_undefined = 0
    for animal in array :
        sheep += 1 if animal == True else 0
        null_or_undefined += 1 if animal == False else 0

    return present , null_or_undefined


array = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

print(count(array))
