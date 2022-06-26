
def is_valid(index, sequence):
    return 0 <= index < len(sequence)

def add(str_input, sequence):
    if str_input not in sequence:
        sequence.append(str_input)
        print(success_add)
        return sequence
    print(already_there)

def remove(str_input, sequence):
    if str_input in sequence:
        sequence.remove(str_input)
        print(success_remove)
        return sequence
    print(card_not)

def remove_at(index, sequence):
    if is_valid(index, sequence):
        sequence.pop(index)
        print(success_remove)
        return sequence
    print(index_not)

def insert(index, str_input, sequence):
    if is_valid(index, sequence):
        if str_input in sequence:
            print('Card is already added')
            return
        sequence.insert(index, str_input)
        print(success_add)
        return sequence
        # print('Card is already in the deck')
    print(index_not)
        
def command_func(lst, sequence):
    command = lst[0]
    if command == 'Add':
        card_name = lst[1]
        result = add(card_name, sequence)
    elif command == 'Remove':
        card_name = lst[1]
        result = remove(card_name, sequence)
    elif command == 'Remove At':
        index = int(lst[1])
        result = remove_at(index, sequence)
    elif command == 'Insert':
        index = int(lst[1])
        card_name = lst[2]
        result = insert(index, card_name, sequence)
    return result


cards = input().split(', ')
num = int(input())
success_add = 'Card successfully added'
success_remove = 'Card successfully removed'
already_there = 'Card is already in the deck'
card_not = 'Card not found'
index_not = 'Index out of range'

for _ in range(num):
    command_list = input().split(', ')
    command_func(command_list, cards)

print(', '.join(cards))
