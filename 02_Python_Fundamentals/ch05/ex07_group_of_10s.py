'''
Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and
prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.

Hints
•	Keep track of the group using a variable to store its max value.
•	Create a loop and filter the elements that are less than or equal to the group boundary and remove them from the original list.
•	Increase the boundary by 10.
•	Loop until the given list is empty.
'''


group_sequence = list(map(int, input().split(', ')))
max_value = len(group_sequence)
group_boundary = 10
while max_value > 0:
    filtered_group = list(filter(lambda x: x <= group_boundary, group_sequence))
    for item in filtered_group:
        group_sequence.remove(item)

    print(f"Group of {group_boundary}'s: {filtered_group}")

    max_value -= len(filtered_group)
    group_boundary += 10
