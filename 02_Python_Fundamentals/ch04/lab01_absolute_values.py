# numbers = input().split(' ')
# abs_numbers = []
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
# print(abs_numbers)

# numbers = list(map(float, input().split(' ')))
# print(numbers)


# result = [abs(num) for num in numbers]
# print(result)

def countdown(number):
    print(number)

    if number == 0:
        return
    countdown(number - 1)

countdown(5)