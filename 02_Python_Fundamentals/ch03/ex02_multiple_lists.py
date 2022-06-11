'''
Write a program that receives two numbers (factor and count).
It should create a list with a length of the given count that contains only integer numbers,
which are multiples of the given factor. The numbers should be only positive,
and they should be arranged in ascending order, starting from the value of the factor.
'''

def is_multiple(num, fac):
    return num % fac == 0

def is_positive(num):
    return num >= 0

factor = int(input())
count = int(input())

result = []
cur_num = factor

while len(result) < count:
    if is_multiple(cur_num, factor) and is_positive(cur_num):
        result.append(cur_num)
    cur_num += 1

print(sorted(result,reverse=False))
