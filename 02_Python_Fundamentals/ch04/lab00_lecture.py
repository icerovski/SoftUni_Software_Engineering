# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)

# numbers = list(map(int, input().split(', ')))
# print(numbers)

def comma_cleanup(line):
    if line:
        digit = ""
        for char in line:
            if char != ",":
                digit += char
            else:
                continue
    else:
        digit = 0

    return digit

my_string = '1,234'
print(comma_cleanup(my_string))
print(type(comma_cleanup(my_string)))


add_fun = lambda a= 20: lambda b: a + b
print(add_fun(30))


def calculator(num1, num2, operator):
    calc_dict = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y
    }

    return calc_dict[operator](num1, num2)

a = int(input())
b = int(input())
operator_input = input()

print(calculator(a, b, operator_input))

