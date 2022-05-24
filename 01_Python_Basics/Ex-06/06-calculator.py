n1 = int(input())
n2 = int(input())
op = input()

def is_odd(x):
    '''Check if number is odd or even'''
    if x % 2 == 0:
        return "even"
    return "odd"

if op == "+":
    result = n1 + n2
    print(f'{n1} {op} {n2} = {result} - {is_odd(result)}')
elif op == "-":
    result = n1 - n2
    print(f'{n1} {op} {n2} = {result} - {is_odd(result)}')
elif op == "*":
    result = n1 * n2
    print(f'{n1} {op} {n2} = {result} - {is_odd(result)}')
elif op == "/":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} {op} {n2} = {result:.2f}')
elif op == "%":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} {op} {n2} = {result}')
