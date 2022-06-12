'''
Write a function that calculates the total price of an order and returns it.
The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
The prices for a single piece of each product are: 
•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00

Print the result formatted to the second decimal place.

'''

item = input()
count = int(input())
items_prices = {
    'coffee':1.5,
    'water':1.00,
    'coke':1.40,
    'snacks':2.00
}

print(f'{items_prices[item] * count:.2f}')