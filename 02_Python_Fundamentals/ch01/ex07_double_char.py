'''
You will be given strings until you receive the command "End". For each string given,
you should print a string in which each character (case-sensitive) is repeated twice.
Note that if you receive the string "SoftUni", you should NOT print it!
'''

INPUT_STRING = input()

while INPUT_STRING != 'End':
    if INPUT_STRING != 'SoftUni':
        for char in INPUT_STRING:
            print(2 * char, end='')
        print()

    INPUT_STRING = input()
