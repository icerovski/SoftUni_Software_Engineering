width = int(input())
length = int(input())
cake_size = width * length
piece_size = 1
remaining_pieces = cake_size

no_cake_left = True

while remaining_pieces >= 0:
    cake_round = input()
    if cake_round == 'STOP':
        no_cake_left = False
        break
    else:
        remaining_pieces = remaining_pieces - int(cake_round)


if no_cake_left:
    print(f'No more cake left! You need {-remaining_pieces} pieces more.')
else:
    print(f'{remaining_pieces} pieces are left.')