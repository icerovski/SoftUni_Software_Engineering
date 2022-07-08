'''
You seem to be doing great at your first job, so your boss decides to give you as your next task something more
challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.
You will be receiving key-value pairs on separate lines separated by ": " until you receive the command
"statistics". Sometimes you may receive a product more than once. In that case, you have to add the new
quantity to the existing one. When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
- {productN}: {quantityN}
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"
'''
food_stock = {}
while True:
    line_input_raw = input()
    if line_input_raw == 'statistics':
        break

    key_value_pair = line_input_raw.split(': ')
    key = key_value_pair[0]
    value = int(key_value_pair[1])
    if key in food_stock:
        food_stock[key] += value
    else:
        food_stock[key] = value

count_all_products = len(food_stock.values())
sum_all_quantities = sum(food_stock.values())
print(f'Products in stock:')
products_list = [f'- {key}: {value}' for (key, value) in food_stock.items()]
print('\n'.join(products_list))
print(f'Total Products: {count_all_products}')
print(f'Total Quantity: {sum_all_quantities}')
