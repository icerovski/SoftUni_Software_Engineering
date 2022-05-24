target_profit = int(input())
service_type = input()

profit = 0
cum_profit = 0
goal_is_reached = False
while service_type != 'closed':
    if service_type == 'haircut':
        sub_service_type = input()
        if sub_service_type == 'mens':
            profit = 15
        elif sub_service_type == 'ladies':
            profit = 20
        elif sub_service_type == 'kids':
            profit = 10
    elif service_type == 'color':
        sub_service_type = input()
        if sub_service_type == 'touch up':
            profit = 20
        elif sub_service_type == 'full color':
            profit = 30

    cum_profit += profit
    if target_profit <= cum_profit:
        goal_is_reached = True
        break

    service_type = input()

if goal_is_reached:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {target_profit - cum_profit}lv. more.')

print(f'Earned money: {cum_profit}lv.')