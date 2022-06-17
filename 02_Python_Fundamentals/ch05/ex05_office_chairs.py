'''
You are a facility manager at a large business center. One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
On the first line, you will be given an integer n representing the number of rooms in the business center. On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors). 
Keep track of the free chairs:
•	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
•	Otherwise, print: "Game On, {total_free_chairs} free chairs left".
'''

rooms_count = int(input())
free_chairs = 0
for n in range(1, rooms_count + 1):
    room_setup = input().split(' ')
    room_chairs = room_setup[0].count('X')
    people_visiting = int(room_setup[1])
    needed_chairs_in_room = room_chairs - people_visiting
    if needed_chairs_in_room < 0:
        print(f'{abs(needed_chairs_in_room)} more chairs needed in room {n}')

    free_chairs +=  needed_chairs_in_room

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')
