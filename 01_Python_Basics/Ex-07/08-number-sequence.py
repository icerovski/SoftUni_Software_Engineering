nums_count = int(input())
num = int(input()) # the first number is given outside the loop
max_num = num # assign it to the max value
min_num = num # also assign it to the min value

nums_count -= 1 # decrease the count by one, which was given outside the loop
while nums_count > 0:
    num = int(input())
    if num > max_num: max_num = num
    elif num < min_num: min_num = num
    nums_count -= 1

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')