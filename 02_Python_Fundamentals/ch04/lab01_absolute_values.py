'''
Write a program that receives a sequence of numbers, separated by a single space, and
prints their absolute value as a list. Use abs().
'''
def absolute(x):
    return abs(x)

sequence = list(map(float, input().split(' ')))
abs_sequence = list(map(absolute, sequence))
print(abs_sequence)