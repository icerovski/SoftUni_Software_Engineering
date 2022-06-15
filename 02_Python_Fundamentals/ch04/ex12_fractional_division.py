'''
Write a function that receives two integer numbers. Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.
Hints
•	Read more about factorial here: https://en.wikipedia.org/wiki/Factorial 
'''

# def recursive_split(number, cummulative_numbers):
#     cummulative_numbers.append(number % 10) # append the last digit
#     number = number // 10 # remove the last digit
#     if number != 0:
#         return recursive_split(number, cummulative_numbers)
#     return cummulative_numbers

def recursive_factorial(num, cummulative_product=1):
    # we start with cummulative_product = 1, so we stop the recurssion after we calculate with 2
    if num < 2:
        return cummulative_product

    cummulative_product *= num
    return recursive_factorial(num - 1, cummulative_product)

int_one = int(input())
int_two = int(input())

result = recursive_factorial(int_one) / recursive_factorial(int_two)
print(f'{result:.2f}')
