from sys import maxsize

count = int(input())
max_num = -1 * maxsize
sum_nums = 0

for i in range(0, count):
    num = int(input())
    if num > max_num: max_num = num
    sum_nums += num

sum_nums -= max_num
difference = abs(sum_nums - max_num)
if difference == 0:
    print(f'Yes\nSum = {sum_nums}')
else:
    print(f'No\nDiff = {difference}')
