'''
Calculate how many courses will be needed to elevate N persons by using an elevator
with a capacity of P persons. The input holds two lines: the number of people N and
the capacity P of the elevator.
'''

from math import ceil

people_count = int(input())
elevator_capacity = int(input())

# Solution 1 - Time 0.030s
people_remaining = people_count
number_of_elevator_rides = 0
while people_remaining > 0:
    people_remaining -= elevator_capacity
    number_of_elevator_rides += 1
print(number_of_elevator_rides)

# Solution 2 - Time 0.100s
number_of_elevator_rides = int(people_count / elevator_capacity)
if people_count % elevator_capacity != 0:
    number_of_elevator_rides += 1
print(number_of_elevator_rides)

# Solution 3 - Time 0.070s
number_of_elevator_rides = ceil(people_count / elevator_capacity)
print(number_of_elevator_rides)

# Solution 4
number_of_elevator_rides = 0 if elevator_capacity == 0 else ceil(people_count / elevator_capacity)
print(number_of_elevator_rides)
