'''
Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in the sequence, sorted in descending order.

Input

· Read from the console a single line holding space-separated integers.

Output

· Print the above-described numbers on a single line, space-separated.

· If less than 5 numbers hold the property mentioned above, print less than 5 numbers.

· Print "No" if no numbers hold the above property.

Constraints

· All input numbers are integers in the range [-1 000 000 … 1 000 000].

· The count of numbers is in the range [1…10 000].
'''

def top_list(fltr_list, count):
    end = min(len(fltr_list), count)
    return [str(num) for num in sorted(fltr_list, reverse=True)[:end]]


numbers = [int(num) for num in input().split(' ')]
numbers_average = sum(numbers) / len(numbers)
filtered = list(filter(lambda x: x > numbers_average, numbers))
top_count = 5

if not filtered:
    print('No')
else:
    print(' '.join(top_list(filtered, top_count)))
