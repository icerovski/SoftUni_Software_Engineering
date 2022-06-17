'''
Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
'''

numbers = list(map(int, input().split(', ')))
positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

outputs = {
    'Positive': ', '.join(map(str, positive)),
    'Negative': ', '.join(map(str, negative)),
    'Even': ', '.join(map(str, even)),
    'Odd': ', '.join(map(str, odd)),
}

for k, v in outputs.items():
    print(f'{k}: {v}')
