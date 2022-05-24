num_sequence_length = int(input())

sum_arr = []

for i in range(0, 2):
    sum = 0
    for j in range(0, num_sequence_length):
        num = int(input())
        sum += num

    sum_arr.append(sum)

difference = abs(sum_arr[0] - sum_arr[1])
if difference == 0:
    print(f'Yes, sum = {sum_arr[0]}')
else:
    print(f'No, diff = {difference}')