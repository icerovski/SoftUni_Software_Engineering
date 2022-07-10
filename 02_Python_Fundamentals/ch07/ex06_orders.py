'''
Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
•	If the product doesn't exist yet, add it with its starting quantity.
•	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. 
Finally, print all items with their names and the total price of each product. 
Input
•	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
•	The product data is always delimited by a single space.
Output
•	Print information about each product in the following format: 
"{product_name} -> {total_price}"
•	Format the total price to the 2nd digit after the decimal separator.
'''


def update_orders(lst):
    name = lst[0]
    price = lst[1]
    quantity = lst[2]

    if name not in orders.keys():
        orders[name] = {'price': 0, 'quantity' : 0, 'total_cost' : 0}
    orders[name]['quantity'] += int(quantity)
    orders[name]['price'] = float(price)
    orders[name]['total_cost'] = orders[name]['quantity'] * orders[name]['price']
    


orders = {}
while True:
    command = input()
    if command == 'buy':
        break
    new_info = command.split(' ')
    update_orders(new_info)

for k, v in orders.items():
    print(f'{k} -> {v["total_cost"]:.2f}')
