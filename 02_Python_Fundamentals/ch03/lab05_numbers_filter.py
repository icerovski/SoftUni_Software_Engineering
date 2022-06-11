'''
On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

For further instructions: https://realpython.com/python-filter-function/
'''

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def is_negative(number):
    return number < 0

def is_positive(number):
    return number >= 0

def perform_function(instruction):
    result = None
    if instruction == 'even':
        result = is_even
    elif instruction == 'odd':
        result = is_odd
    elif instruction == 'negative':
        result = is_negative
    elif instruction == 'positive':
        result = is_positive
    return result

line_count = int(input())
num_list = []
while line_count > 0:
    num_list.append(int(input()))
    line_count -= 1

# https://www.geeksforgeeks.org/assign-function-to-a-variable-in-python/
action = input()
current_function = perform_function(action)

filtered = list(filter(perform_function(action), num_list))
print(filtered)
