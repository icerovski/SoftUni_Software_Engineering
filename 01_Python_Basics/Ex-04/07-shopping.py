budget = float(input())
count_N = int(input())
count_M = int(input())
count_P = int(input())

price_N = 250

cost_N = count_N * price_N
cost_M = count_M * 0.35 * cost_N
cost_P = count_P * 0.1 * cost_N

if count_N > count_M:
    cost_total = (cost_N + cost_M + cost_P) * (1 - 0.15)
else:
    cost_total = (cost_N + cost_M + cost_P)

if budget - cost_total >= 0:
    print(f'You have {budget - cost_total:.2f} leva left!')
else:
    print(f'Not enough money! You need {cost_total - budget:.2f} leva more!')
