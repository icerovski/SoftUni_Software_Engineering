'''
You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
You will receive a collection of items and a budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a specific price, which is given below:
Type	Maximum Price
Clothes	50.00
Shoes	35.00
Accessories	20.50
If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough for buying the train ticket.

Input / Constraints
•	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
•	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
Output
•	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
"{price1} {price2} {price3} … {priceN}"
•	Second, print the profit, formatted to the second decimal point in the following format:
"Profit: {profit}"
•	Finally:
o	If the budget is enough for buying the train ticket, print: "Hello, France!" 
o	Otherwise, print: "Not enough money."
'''

items = input().split('|')
budget = float(input())
ticket = 150.00

bought_items = []
total_revenue = 0
total_cost = 0
total_profit = 0

for item in items:
    type_price_pair = item.split('->')
    item_type = type_price_pair[0]
    item_price = float(type_price_pair[1])

    if item_type == 'Clothes' and item_price > 50.00:
        continue
    elif item_type == 'Shoes' and item_price > 35.00:
        continue
    elif item_type == 'Accessories' and item_price > 20.50:
        continue

    if budget < item_price:
        continue

    budget -= item_price
    total_cost += item_price

    item_revenue = 1.4 * item_price
    total_revenue += item_revenue
    bought_items.append(f'{item_revenue:.2f}')

total_profit = total_revenue - total_cost
budget += total_revenue

print(' '.join(bought_items))
print(f'Profit: {total_profit:.2f}')
if budget >= ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
