
def is_valid(index, sequence):
    return 0 <= index < len(sequence)

def blacklist(str_input, sequence):
    if str_input in sequence:
        index = sequence.index(str_input)
        sequence.pop(index)
        sequence.insert(index, 'Blacklisted')
        blacklisted.append(str_input)
        print(f'{str_input} was blacklisted.')
    else:
        print(f'{str_input} was not found.')
    return sequence

def error(index, sequence):
    if is_valid(index, sequence):
        name = sequence[index]
        if name not in ('Blacklisted', 'Lost'):
            sequence.pop(index)
            sequence.insert(index, 'Lost')
            lost.append(name)
            print(f'{name} was lost due to an error.')
            return sequence

def change(index, str_input, sequence):
    if is_valid(index, sequence):
        name = sequence[index]
        sequence[index] = str_input
        print(f'{name} changed his username to {str_input}.')
        return sequence

def command_func(lst, sequence):
    command = lst[0]
    if command == 'Blacklist':
        name = lst[1]
        result = blacklist(name, sequence)
    elif command == 'Error':
        index = int(lst[1])
        result = error(index, sequence)
    elif command == 'Change':
        index = int(lst[1])
        new_name = lst[2]
        result = change(index, new_name, sequence)
    return result


friends = input().split(', ')
blacklisted = []
lost = []

while True:
    command_str = input()
    if command_str == 'Report':
        print(f'Blacklisted names: {len(blacklisted)}')
        print(f'Lost names: {len(lost)}')
        print(' '.join(friends))
        break
    
    command_list = command_str.split(' ')
    command_func(command_list, friends)