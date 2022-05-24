lily_age = int(input())
price_of_washer = float(input())
price_per_toy = int(input())

money = 0
money_per_birthday_increase = 10
money_per_birthday_decrease = 1

toys = 0
toys_per_birthday = 1

for i in range(1, lily_age + 1):
    if i % 2 != 0: 
        toys += toys_per_birthday
    else: 
        j = i / 2 # count of birthdays where she receives money
        money += j * money_per_birthday_increase
        money -= money_per_birthday_decrease

toys_money = toys * price_per_toy
budget = money + toys_money

difference = abs(price_of_washer - budget)

if budget >= price_of_washer:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')