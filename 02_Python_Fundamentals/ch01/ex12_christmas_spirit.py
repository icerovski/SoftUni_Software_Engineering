'''
It is time to get in a Christmas mood. You need to decorate the house in time for the big event,
but you have limited days to do so.

Write a program that calculates how much money you will need to spend on Christmas decorations
and how much your Christmas spirit will improve.

Conditions are very long, so I will not paste them..
'''

QUANTITY = int(input())
DAYS = int(input())

ORNAMENT_PRICE = 2
ORNAMENT_POINTS = 5
TREE_SKIRT_PRICE = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_PRICE = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_PRICE = 15
TREE_LIGHTS_POINTS = 17

budget = 0
points = 0

for i in range(1, DAYS + 1):
    if i % 11 == 0:
        QUANTITY += 2

    if i % 2 == 0:
        budget += QUANTITY * ORNAMENT_PRICE
        points += ORNAMENT_POINTS

    if i % 3 == 0:
        budget += QUANTITY * (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE)
        points += TREE_SKIRT_POINTS + TREE_GARLAND_POINTS

    if i % 5 == 0:
        budget += QUANTITY * TREE_LIGHTS_PRICE
        points += TREE_LIGHTS_POINTS
        if i % 3 == 0:
            points += 30

    if i % 10 == 0:
        points -= 20
        budget += 1 * (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE)

if DAYS % 10 == 0:
    points -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {points}')
