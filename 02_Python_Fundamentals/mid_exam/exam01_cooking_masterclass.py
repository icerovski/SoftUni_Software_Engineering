from math import ceil

budget = float(input())
students = int(input())
price_pack_of_flour = float(input())
price_single_egg = float(input())
price_single_apron = float(input())

# FLOUR
# every fifth package of flour is free
free_flour_packages = students // 5
cost_flour = (students - free_flour_packages) * price_pack_of_flour

# EGGS
cost_eggs = students * price_single_egg * 10

# APRONS
# get 20% more aprons, rounded up to the next integer
number_of_aprons = ceil(students * 1.2)
cost_aprons = number_of_aprons * price_single_apron 

total_cost = cost_flour + cost_eggs + cost_aprons

if total_cost <= budget:
    print(f'Items purchased for {total_cost:.2f}$.')
else:
    needed_money = total_cost - budget
    print(f'{needed_money:.2f}$ more needed.')
