'''
Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.
'''

nums = list(map(int, input().split(', ')))
# even_indeces = [nums.index(num) for num in nums if num % 2 == 0]

found_indices_or_no = map(
    lambda x: x if nums[x] % 2 == 0 else 'no',
    range(len(nums))
)
print(list(found_indices_or_no))
even_indeces = list(filter(lambda a: a != 'no', found_indices_or_no))

print(even_indeces)
