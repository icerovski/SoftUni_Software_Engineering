'''
Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
Print the new text string after removing the vowels.
The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
'''

txt = input()
vowels = ['a', 'o', 'u', 'e', 'i']
filtered = [char for char in txt if char.lower() not in vowels]
print(''.join(filtered))

filtered_02 = list(filter(lambda char: char.lower() not in vowels, txt))
print(''.join(filtered_02))
