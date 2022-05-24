width = int(input())
length = int(input())
height = int(input())
apartment_space = width * length * height
# free_space = apartment_space

box_size = 1
is_enough_space = False

while apartment_space >= 0:
    action = input()
    if action == 'Done':
        is_enough_space = True
        break
    else:
        apartment_space -= int(action)

if not is_enough_space:
    print(f'No more free space! You need {-apartment_space} Cubic meters more.')
else:
    print(f'{apartment_space} Cubic meters left.')