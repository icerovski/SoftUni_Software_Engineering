num_count = int(input())
odd_sum = 0
even_sum = 0

for i in range(0, num_count):
    num = int(input())
    if i % 2 != 0:
        odd_sum += num
    else:
        even_sum += num

difference = abs(odd_sum - even_sum)
if difference == 0:
    print(f'Yes\nSum = {odd_sum}')
else:
    print(f'No\nDiff = {difference}')