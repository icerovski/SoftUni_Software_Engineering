'''
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times
the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
'''

INPUT_STR = input()
LOWER_CASE_STR = INPUT_STR.casefold()
COUNTER = 0

for word in ('sand', 'water', 'fish', 'sun'):
    COUNTER += LOWER_CASE_STR.count(word)

print(COUNTER)
