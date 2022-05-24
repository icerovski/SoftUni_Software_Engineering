'''
You will be given number n. After that, you'll receive different strings n times.
Your task is to check if the given strings are pure, meaning that they do NOT consist
of any of the characters: comma ",", period ".", or underscore "_":
•	If a string is pure, print "{string} is pure."
•	Otherwise, print "{string} is not pure!"
'''

NUM = int(input())
COMMA = ','
PERIOD = '.'
UNDERSCORE = '_'

for i in range(0, NUM):
    IS_PURE = True
    input_string = input()
    # for char in input_string:
    #     if char in (COMMA, PERIOD, UNDERSCORE):
    #     # if char == COMMA or char == PERIOD or char == UNDERSCORE:
    #         IS_PURE = False
    #         break
    # if IS_PURE:
    #     print(f'{input_string} is pure.')
    # else:
    #     print(f'{input_string} is not pure!')


    if COMMA in input_string or PERIOD in input_string or UNDERSCORE in input_string:
        print(f'{input_string} is pure.')
    else:
        print(f'{input_string} is not pure!')