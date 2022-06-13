'''
Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a list of only the even numbers. Use filter().
'''

is_even = lambda x: x % 2 == 0
numbers = list(map(int, input().split(' ')))
filtered = list(filter(is_even, numbers))

print(filtered)
