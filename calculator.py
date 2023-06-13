"""
https://www.codewars.com/kata/57356c55867b9b7a60000bd7
The problem :
    Create an basic function which take 3 argument operation and two numbers

    exemple:
    calculate ( '+' , 89, 83)

"""

def calculate(operation , number1 , number2 ):
    if str(operation) == operation  and int(number1) == number1 and int(number2) == number2:
        operation = str(number1) + operation + str(number2)
        result = eval(f"{operation}" )
    return result if result else "Please Enter Valid Arguments"


print(calculate('+' , 40 , 30))
print(calculate('-' , 40 , 30))
print(calculate('/' , 2 , 3))
