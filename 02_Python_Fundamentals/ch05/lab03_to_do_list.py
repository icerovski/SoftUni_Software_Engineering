'''
You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}". 
Return a list containing all to-do notes sorted by importance in ascending order. 
The importance value will always be an integer between 1 and 10 (inclusive).
Hint
•	Use the pop() and insert() methods.
'''

notes = [0] * 10
while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split('-')
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)
