# Assumes that first input is always a number
min = int(input())
line = input()
while line != "Stop":
    num = int(line)
    if min > num: min = num
    
    line = input()

print(min)