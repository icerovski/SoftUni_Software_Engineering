'''
You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative, positive, or zero.
Try to do this WITHOUT multiplying the 3 numbers.
'''

def multiplication_sign(tpl):
    if 0 in numbers:
        return 'zero'

    negative_num_count = len(list(filter(lambda x: x<0, tpl)))
    if negative_num_count % 2 != 0:
        result = 'negative'
    else:
        result = 'positive'
    return result

num_one = int(input())
num_two = int(input())
num_three = int(input())

numbers = (num_one, num_two, num_three)
print(multiplication_sign(numbers))
