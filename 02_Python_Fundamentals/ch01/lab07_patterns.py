'''Write a program that receives a number and creates the following pattern.
The number represents the largest count of stars on one row.'''

NUM = int(input())
MARKER = '*'

for i in range(1, NUM + 1, 1):
    result = i * MARKER
    print(result)

for i in range(NUM - 1, 0, -1):
    result = i * MARKER
    print(result)
