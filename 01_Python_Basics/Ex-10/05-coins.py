change = float(input())
counter = 0

coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

for i in range (0, len(coins)):
    base = change // coins[i]
    if base != 0:
        counter += base
        change = round(change % coins[i], 2)

print(int(counter))