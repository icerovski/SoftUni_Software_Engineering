'''
Write a program that prints all elements from a given sequence of words that occur an odd number of times (caseinsensitive)
in it.
• Words are given on a single line, space-separated.
• Print the result elements in lowercase, in their order of appearance.
'''

words = list(map(lambda w: w.lower(), input().split(' ')))
dictionary = {}
for word in words:
    if word not in dictionary.keys():
        dictionary[word] = 0
    dictionary[word] += 1

for k, v in dictionary.items():
    if v % 2 != 0:
        print(k, end= ' ')
