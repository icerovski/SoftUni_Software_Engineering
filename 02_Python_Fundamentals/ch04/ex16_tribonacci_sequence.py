'''
In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. 
You will receive a positive integer number as input.
'''
# slicing function tutorial
# https://www.w3schools.com/python/ref_func_slice.asp

sequence_length = int(input())
tri = 3
tribonaci_sequence = []
for i in range(sequence_length):
    if i == 0:
        tribonaci_sequence += [1]
        continue
    start = i - min(tri, i)
    count = slice(start, i)
    tribonaci = sum(tribonaci_sequence[count])
    tribonaci_sequence += [tribonaci]

print(' '.join(list(map(str, tribonaci_sequence))))
