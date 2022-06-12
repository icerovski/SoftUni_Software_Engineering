'''
Write a program that receives a list of integer numbers (separated by a single space) and a number n.
The number n represents the count of numbers to remove from the list.
You should remove the smallest ones, and then, you should print all the numbers that are left in the list,
separated by a comma and a space ", ".
'''
num_list = list(map(int, input().split(' ')))
numbers_to_remove = int(input())

sorted_num_list = sorted(num_list)
smallest_numbers_to_remove = sorted_num_list[:numbers_to_remove]
new_list = list(filter(lambda x: x not in smallest_numbers_to_remove, num_list))

new_list_str = list(map(str, new_list))
separator = ', '
print(separator.join(new_list_str))
