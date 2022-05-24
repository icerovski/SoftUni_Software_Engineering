tshirt_price = float(input())
bill_to_get_present = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (tshirt_price + shorts_price) * 2
discount = 0.15

cost_of_outfit = tshirt_price + shorts_price + socks_price + shoes_price
discount_cost_of_outfit = cost_of_outfit * (1 - discount)

if discount_cost_of_outfit >= bill_to_get_present:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {discount_cost_of_outfit:.2f} lv.')
else:
    funds_short = bill_to_get_present - discount_cost_of_outfit
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {funds_short:.2f} lv. more.')