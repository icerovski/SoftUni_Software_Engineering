'''
Help out the sorting hat to sort the new students in the houses of Hogwarts.
You will be receiving names until the command "Welcome!".
The length of each name determines in which house the student is going:
•	If the name is less than 5 chars, the student is going into Gryffindor
    o	Print "{name} goes to Gryffindor."
•	If the name is exactly 5 chars, the student is going into Slytherin
    o	Print "{name} goes to Slytherin."
•	If the name is exactly 6 chars, the student is going into Ravenclaw
    o	Print "{name} goes to Ravenclaw."
•	If the name is more than 6 chars, the student is going into Hufflepuff
    o	Print "{name} goes to Hufflepuff."

While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end
the program. No more sorting for today! If all students are sorted successfully, print
"Welcome to Hogwarts."
'''

NAMES = input()

while NAMES != 'Welcome!':
    if NAMES == 'Voldemort':
        print('You must not speak of that name!')
        break

    LEN = len(NAMES)
    if LEN < 5:
        print(f'{NAMES} goes to Gryffindor.')
    elif LEN == 5:
        print(f'{NAMES} goes to Slytherin.')
    elif LEN == 6:
        print(f'{NAMES} goes to Ravenclaw.')
    elif LEN > 6:
        print(f'{NAMES} goes to Hufflepuff.')

    NAMES = input()

else:
    print('Welcome to Hogwarts.')
    