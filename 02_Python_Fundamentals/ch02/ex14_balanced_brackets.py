'''
On the first line, you will receive n – the number of lines, which will follow.
On the following n lines, you will receive one of the following:
•	Opening bracket – "(",
•	Closing bracket – ")" or
•	Random string
Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one.
Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as UNBALANCED.
You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
'''

num = int(input())
new_string = ''
is_balanced = False

# We only need the brackets
for i in range(num):
    str_input = input()
    if str_input == '(' or str_input == ')':
        new_string += str_input

# No brackets is UNBALANCED
# Nested brackets is UNBALANCED
# Starting with ')' is UNBALANCED
# Only way its balanced is if starts with '()'
for i in range(0, len(new_string), 2):
    if new_string[i] == '(' and new_string[i + 1] == ')':
        is_balanced = True
    else:
        is_balanced = False
        break

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
