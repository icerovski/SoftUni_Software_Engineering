'''
You have a water tank with a capacity of 255 liters. On the first line, you will receive n –
the number of lines, which will follow. On the following n lines, you will receive liters of
water (integers), which you should pour into your tank. If the capacity is not enough, print
"Insufficient capacity!" and continue reading the next line.
On the last line, print the liters in the tank.
'''

NUM = int(input())
CAPACITY = 255
liters_in_tank = 0

for _ in range(NUM):
    new_liters = int(input())
    if liters_in_tank + new_liters > CAPACITY:
        print('Insufficient capacity!')
    else:
        liters_in_tank += new_liters

print(liters_in_tank)
