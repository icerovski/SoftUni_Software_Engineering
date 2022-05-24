''''Write a program that reads different floating-point numbers from the console.
When it receives a number between 1 and 100 inclusive, the program should stop reading
and should print "The number {number} is between 1 and 100".'''

NUM = float(input())
while NUM < 1 or NUM > 100:
    NUM = float(input())

print(f'The number {NUM} is between 1 and 100')
