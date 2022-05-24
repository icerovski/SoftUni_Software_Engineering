from functools import reduce

puzzle = 2.6
doll = 3
bear = 4.1
minion = 8.2
truck = 2

trip_cost = float(input())
puzzle_num = int(input())
doll_num = int(input())
bear_num = int(input())
minion_num = int(input())
truck_num = int(input())

prices = [puzzle, doll, bear, minion, truck]
nums = [puzzle_num, doll_num, bear_num, minion_num, truck_num]

revenue = reduce(lambda x, y: x + y, 
            list(map(lambda x, y: x * y, prices, nums)))

total_items = reduce(lambda x, y: x + y, nums)
if total_items >= 50:
    revenue = (1 - 0.25) * revenue

rent_cost = 0.1 * revenue

net_profit = revenue - rent_cost - trip_cost

if net_profit >= 0:
    print(f'Yes! {net_profit:.2f} lv left.')
else:
    print(f'Not enough money! {-1 * net_profit:.2f} lv needed.')