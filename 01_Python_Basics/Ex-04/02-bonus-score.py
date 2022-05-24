num = int(input())

if num <= 100:
    bonus = 5
elif num > 100 and num <= 1000:
    bonus = 0.2 * num
elif num > 1000:
    bonus = 0.1 * num

if num % 2 == 0:
    bonus += 1

if str(num)[-1] == '5':
    bonus += 2

print(bonus)
print(bonus + num)