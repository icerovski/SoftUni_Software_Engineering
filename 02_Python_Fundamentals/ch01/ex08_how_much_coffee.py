'''
Everybody knows that you spend too much time awake during nighttime.
Your task is to define how much coffee you need to stay awake. Until you receive the command "END",
you need to read commands on different lines. According to the commands, calculate the number of
coffees you need to drink to stay awake during the daytime.

The list of events can contain the following:
•	You have homework to do ("coding").
•	You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
•	You watch a movie ("movie").
•	If other events are present, they will be represented by arbitrary strings. Just ignore them!

Each event can be lowercase or uppercase:
•	If it is lowercase, you need 1 coffee by an event.
•	If it is uppercase, you need 2 coffees by an event.

In the end, print the number of coffees you will need. If the count has exceeded 5, just print
"You need extra sleep".
'''

counter = 0
COMMANDS = input()

while COMMANDS != 'END':
    if COMMANDS.lower() in ('coding', 'dog', 'cat', 'movie'):
        if COMMANDS.islower():
            counter += 1
        elif COMMANDS.isupper():
            counter += 2

    COMMANDS = input()

if counter > 5:
    print('You need extra sleep')
else:
    print(f'{counter}')
