'''
You are saying goodbye to your best friend: "See you next happy year".
Happy Year is the year with only distinct digits, for example, 2018.
Write a program that receives an integer number and finds the next happy year.
'''

number = int(input())
digits_are_distinct = False

while not digits_are_distinct:
    number += 1
    test_number = number

    while test_number > 0:
        cur_digit = test_number % 10
        test_number = int(test_number / 10)

        cur_digit_str = str(cur_digit)
        test_number_str = str(test_number)

        if cur_digit_str in test_number_str:
            break
    else:
        digits_are_distinct = True
        print(number)
