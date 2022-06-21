'''
Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".
Print the result on the console.
'''


def float_function(param):
    return f'{float(param) * 1.5:.2f}'

def int_function(param):
    return int(param) * 2

def str_function(param):
    return '$' + str(param) + '$'


type = input()
value = input()
if type == 'real':
    print(float_function(value))
elif type == 'int':
    print(int_function(value))
elif type == 'string':
    print(str_function(value))
