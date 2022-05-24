flower_type = input()
flower_count = int(input())
budget = int(input())

if flower_type == 'Roses':
    cost = flower_count * 5
    if flower_count > 80:
        cost = cost * (1 - 0.1)
elif flower_type == 'Dahlias':
    cost = flower_count * 3.8
    if flower_count > 90:
        cost = cost * (1 - 0.15)
elif flower_type == 'Tulips':
    cost = flower_count * 2.8
    if flower_count > 80:
        cost = cost * (1 - 0.15)
elif flower_type == 'Narcissus':
    cost = flower_count * 3
    if flower_count < 120:
        cost = cost * (1 + 0.15)
elif flower_type == 'Gladiolus':
    cost = flower_count * 2.5
    if flower_count < 80:
        cost = cost * (1 + 0.2)

if budget >= cost:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} leva left.')
else:
    print(f'Not enough money, you need {cost - budget:.2f} leva more.')