'''
Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
Create a program that calculates how many loaves you can make with the budget you have.

Conditions are very long, so I will not paste them..
'''

BUDGET = float(input())
FLOUR_PRICE = float(input())
eggs_price = 0.75 * FLOUR_PRICE
milk_price = 1.25 * FLOUR_PRICE
bread_price = FLOUR_PRICE + eggs_price + 0.25 * milk_price

BUDGET -= bread_price
number_of_loaves = 0
colored_eggs = 0

while BUDGET > 0:
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

    BUDGET -= bread_price

money_left = BUDGET + bread_price
print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
