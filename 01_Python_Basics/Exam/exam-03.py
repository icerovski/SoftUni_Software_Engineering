weight = float(input())
service_type = input()
distance = int(input())

price = 0
if weight < 1:
    price = 3
elif 1 <= weight < 10:
    price = 5
elif 10 <= weight < 40:
    price = 10
elif 40 <= weight < 90:
    price = 15
elif 90 <= weight < 150:
    price = 20

# standard_cost = price * distance / 100

markup_cost = 0
if service_type == 'express':
    if weight < 1:
        markup = 0.8
    elif 1 <= weight < 10:
        markup = 0.4
    elif 10 <= weight < 40:
        markup = 0.05
    elif 40 <= weight < 90:
        markup = 0.02
    elif 90 <= weight < 150:
        markup = 0.01
    
    markup_amount = price * markup / 100
    markup_per_distance = markup_amount * weight
    markup_cost = distance * markup_per_distance

cost = price * distance / 100 + markup_cost

print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {cost:.2f} lv.')