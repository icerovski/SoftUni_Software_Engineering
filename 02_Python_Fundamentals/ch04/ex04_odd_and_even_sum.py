'''
You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number.
The result should be returned as a single string in the format: 
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.
'''

from functools import reduce

def recursive_split(number, cummulative_numbers):
    cummulative_numbers.append(number % 10) # append the last digit
    number = number // 10 # remove the last digit
    if number != 0:
        return recursive_split(number, cummulative_numbers)
    return cummulative_numbers

def sum_odd(numbers):
    filtered = list(filter(lambda x: x % 2 != 0, numbers))
    res = 0
    if filtered:
        res = reduce(lambda x, y: x + y, filtered)
    return res

def sum_even(numbers):
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    res = 0
    if filtered:
        res = reduce(lambda x, y: x + y, filtered)
    return res

num = int(input())
numbers = []
recursive_split(num, numbers)

sum_of_odd_digits = sum_odd(numbers)
sum_of_even_digits = sum_even(numbers)

print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')
