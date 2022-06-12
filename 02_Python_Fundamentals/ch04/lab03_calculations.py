'''
Create a function that receives three parameters, calculates a result depending on the given operator, and
returns it. Print the result of the function.
The input comes as three parameters – an operator as a string and two integer numbers.
The operator can be one of the following:  "multiply", "divide", "add", "subtract". 
'''
def calculate(x, y, oper):
    result = None
    if oper == 'multiply':
        result = x * y
    if oper == 'divide':
        result = x // y
    if oper == 'add':
        result = x + y
    if oper == 'subtract':
        result = x - y
    return result
    
oper = input()
x = int(input())
y = int(input())

print(calculate(x, y, oper))