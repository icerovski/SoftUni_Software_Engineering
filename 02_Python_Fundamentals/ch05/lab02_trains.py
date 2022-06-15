'''
You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. Until you receive the command "End", you will receive some of the following commands:
•	"add {people}" – you should add the number of people in the last wagon
•	"insert {index} {people}" - you should add the number of people at the given wagon
•	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
There will be no case in which the index is invalid!
After you receive the "End" command print the train.
'''

wagons = int(input())
# train = [0 for item in range(wagons)]
train = [0] * wagons # a simpler way to generate a list with same values
command = input()

while command != 'End':
    command_list = command.split(' ')
    command_word = command_list[0]
    people = int(command_list[-1])
    if command_word == 'add':
        train[wagons - 1] += people
    elif command_word == 'insert':
        train[int(command_list[1])] += people
    elif command_word == 'leave':
        train[int(command_list[1])] -= people

    command =input()

print(train)
