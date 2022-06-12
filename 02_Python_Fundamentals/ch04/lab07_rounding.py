'''
Write a program that rounds all the given numbers, separated by a single space, and
prints the result as a list. Use round().
'''
nums = list(map(float, input().split(' ')))
result = list(map(lambda x: round(x), nums))
print(result)