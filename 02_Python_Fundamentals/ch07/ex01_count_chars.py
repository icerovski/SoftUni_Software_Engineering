'''
Write a program that counts all characters in a string except for space (" ").
Print all the occurrences in the following format:
"{char} -> {occurrences}"
'''
char_dictionary = {}
line = input().replace(' ', '') # strip all spaces from the input

for char in line:
    if char not in char_dictionary.keys():
        char_dictionary[char] = 0
    char_dictionary[char] += 1

for k, v in char_dictionary.items():
    print(f'{k} -> {v}')
