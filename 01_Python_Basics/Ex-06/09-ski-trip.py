days = int(input())
room_type = input()
rating = input()

ratings_list = ['positive', 'negative']
discount = [0.25, -0.1][ratings_list.index(rating)]

rooms_list = ['room for one person', 'apartment', 'president apartment']
room_price = [18, 25, 35][rooms_list.index(room_type)]


if room_type == 'room for one person':
    cost = room_price * (days - 1) * (1 + discount)
    
elif room_type == 'apartment':
    if days < 10:
        cost = room_price * (days - 1) * (1 - 0.3) * (1 + discount)
    elif 10 <= days <= 15:
        cost = room_price * (days - 1) * (1 - 0.35) * (1 + discount)
    else:
        cost = room_price * (days - 1) * (1 - 0.5) * (1 + discount)
elif room_type == 'president apartment':
    if days < 10:
        cost = room_price * (days - 1) * (1 - 0.1) * (1 + discount)
    elif 10 <= days <= 15:
        cost = room_price * (days - 1) * (1 - 0.15) * (1 + discount)
    else:
        cost = room_price * (days - 1) * (1 - 0.2) * (1 + discount)   

print(f'{cost:.2f}')