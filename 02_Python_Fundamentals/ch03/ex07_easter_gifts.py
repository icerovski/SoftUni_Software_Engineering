'''
As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family.
First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
•	"OutOfStock {gift}"
    o	Find the gifts with this name in your collection, if any, and change their values to "None".  
•	"Required {gift} {index}"
    o	If the index is valid, replace the gift on the given index with the given gift. 
•	"JustInCase {gift}"
    o	Replace the value of your last gift with this one. 
In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
"{gift1} {gift2} {gift3} … {giftn}"
Input / Constraints
•	On the 1st line,  you will receive the names of the gifts, separated by a single space.
•	On the following lines, until the "No Money" command is received, you will be receiving commands.
•	The input will always be valid.
Output
•	Print the gifts in the format described above.
'''
gift_names = input().split(' ')
command_input = input()
# updated_gift_names = []
while command_input != 'No Money':
    command_list = command_input.split(' ')
    command = command_list[0]
    gift_update = command_list[1]
    if command == 'OutOfStock':
        for name in gift_names:
            if name == gift_update:
                name = None
    elif command == 'Required':
        command_index = int(command_list[2])
        if command_index < len(gift_names):
            gift_names[command_index] = gift_update
    elif command == 'JustInCase':
        gift_names[-1] = gift_update

    command_input = input()

print(' '.join(list(filter(None, gift_names))))