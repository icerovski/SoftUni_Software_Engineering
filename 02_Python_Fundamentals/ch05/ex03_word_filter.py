'''
Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even.
Print each word on a new line.
'''

text_input = input().split(' ')
filtered = list(filter(lambda x: len(x) % 2 == 0, text_input))
# print list on a new line
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
print('\n'.join(map(str, filtered)))
