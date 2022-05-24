from math import ceil

movie_name = input()
movie_length = int(input())
break_length = int(input())

lunch_length = break_length / 8
relax_length = break_length / 4

remaining_time = break_length - (lunch_length + relax_length + movie_length)

if remaining_time >= 0:
    print(f'You have enough time to watch {movie_name} and left with {ceil(remaining_time)} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(-1 * remaining_time)} more minutes.")