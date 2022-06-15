'''
You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
Your task is to create a function that returns a loading bar depending on the number you have received in the input.
Print the result on the console. For more clarification, see the examples below.
'''

def construct_indicator(num):
    full_line = num // 10 * '%'
    empty_line = (100 - num) // 10 * '.'
    return '[' + full_line + empty_line + ']'


full_count = int(input())
indicator = construct_indicator(full_count)
if full_count == 100:
    print(f'{full_count}% Complete!')
    print(indicator)
else:
    print(f'{full_count}% {indicator}')
    print('Still loading...')
