'''
You will receive three integer numbers.
Write functions named:
•	sum_numbers() that returns the sum of the first two integers
•	subtract() that returns the difference between the returned result of the first function and the third integer
Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
Print the result of the subtract() function on the console.
'''

def sum_numbers(x, y):
    return x + y

def subtract(x, y):
    return x - y

def add_and_subtract(x, y, z):
    return subtract(sum_numbers(x, y), z)

one = int(input())
two = int(input())
three = int(input())

result = add_and_subtract(one, two, three)
print(result)
