'''
Read two integer numbers and, after that, exchange their values.
Print the variable values before and after the exchange, as shown below:
'''

int_a = int(input())
int_b = int(input())
int_temp = int_a
print('Before:')
print(f'a = {int_a}')
print(f'b = {int_b}')

int_a = int_b
int_b = int_temp
print('After:')
print(f'a = {int_a}')
print(f'b = {int_b}')
