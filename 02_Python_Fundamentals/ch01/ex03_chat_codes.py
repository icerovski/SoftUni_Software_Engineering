'''Create a program that receives the n number of messages sent.
On the following n lines, it will receive integer numbers.
For each number, the program should print a different message:'''

NUM = int(input())

for i in range(0, NUM):
    MESSAGE = int(input())
    if MESSAGE == 88:
        print('Hello')
    elif MESSAGE == 86:
        print('How are you?')
    elif MESSAGE < 86 or MESSAGE == 87:
        print('GREAT!')
    elif MESSAGE > 88:
        print('Bye.')
        