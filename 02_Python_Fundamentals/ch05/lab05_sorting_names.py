'''
Write a program that reads a single string with names separated by comma and space ", ".
Sort the names by their length in descending order.
If 2 or more names have the same length, sort them in ascending order (alphabetically).
Print the resulting list.
'''

names = input().split(', ')
# key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower).
# below iterates over two subkeys
sorted_names = sorted(names, key=lambda x: (-len(x), x))
print(sorted_names)
