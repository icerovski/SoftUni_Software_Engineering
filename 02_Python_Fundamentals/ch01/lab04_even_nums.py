'''Write a program that receives a number n on the first line. On the following n lines,
it receives different integer numbers. If the program receives an odd number,
print "{num} is odd!" and end the program. Otherwise, if all numbers given are even,
print "All numbers are even."'''

num_count = int(input())

for i in range(num_count):
    num = int(input())
    if not num % 2 == 0:
        ALL_NUMBERS_EVEN = False
        print(f'{num} is odd!')
        break

# the 'else' clause is executed when the loop finishes iterrating
# without hitting the 'break' statement
else:
    print('All numbers are even.')
