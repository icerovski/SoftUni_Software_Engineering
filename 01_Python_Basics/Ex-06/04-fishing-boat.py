budget = int(input())
season = input()
fishermen_count = int(input())


if fishermen_count <= 6: discount = 0.1
elif 6 < fishermen_count <= 11: discount = 0.15
elif fishermen_count > 11: discount = 0.25


group_is_even = fishermen_count % 2 == 0
even_group_discount = 0.05

if season == 'Spring':
    cost = 3000 * (1 - discount)
    if group_is_even: cost = cost * (1 - even_group_discount)
elif season == 'Summer':
    cost = 4200 * (1 - discount)
    if group_is_even: cost = cost * (1 - even_group_discount)
elif season == 'Autumn':
    cost = 4200 * (1 - discount)
elif season == 'Winter':
    cost = 2600 * (1 - discount)
    if group_is_even: cost = cost * (1 - even_group_discount)

savings = budget - cost
if savings >= 0:
    print(f'Yes! You have {savings:.2f} leva left.')
else:
    print(f'Not enough money! You need {-1*savings:.2f} leva.')