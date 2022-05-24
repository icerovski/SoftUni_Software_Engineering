# Assumes that first input is always a number
max = int(input())
line = input()
while line != "Stop":
    num = int(line)
    if max < num: max = num
    
    line = input()

print(max)