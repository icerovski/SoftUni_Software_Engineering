budget = float(input())
season = input()

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer': 
        cost = budget * 0.3
        venue = 'Camp'
    elif season == 'winter': 
        cost = budget * 0.7
        venue = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer': 
        cost = budget * 0.4
        venue = 'Camp'
    elif season == 'winter': 
        cost = budget * 0.8
        venue = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    cost = budget * 0.9
    venue = 'Hotel'

print(f'Somewhere in {destination}\n{venue} - {cost:.2f}')
