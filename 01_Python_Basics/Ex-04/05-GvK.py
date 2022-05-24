budget = float(input())
extras = int(input())
costume_price = float(input())

decor = 0.1 * budget
if extras > 150:
    costume_costs = (1 - 0.1) * costume_price * extras
else:
    costume_costs = costume_price * extras

net_result = budget - decor - costume_costs

if net_result < 0:
    print(f'Not enough money!\nWingard needs {-1 * net_result:.2f} leva more.')
else:
    print(f'Action!\nWingard starts filming with {net_result:.2f} leva left.')