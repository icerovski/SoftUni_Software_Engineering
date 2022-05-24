'''
Write a program that reads four integer numbers. It should add the first to the second number,
integer divide the sum by the third number, and multiply the result by the fourth number.
Print the final result.
'''

int_1 = int(input())
int_2 = int(input())
int_3 = int(input())
int_4 = int(input())

result = int((int_1 + int_2) / int_3) * int_4
print(result)
