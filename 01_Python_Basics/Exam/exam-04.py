from math import ceil
number_of_days = int(input())

distance = float(input())
cum_distance = distance
while number_of_days > 0:
    percent_increase = float(input())
    distance *= (1 + percent_increase / 100)

    number_of_days -= 1
    cum_distance += distance

difference = abs(cum_distance - 1000)
if cum_distance >= 1000:
    print(f"You've done a great job running {int(ceil(difference))} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {int(ceil(difference))} more kilometers")