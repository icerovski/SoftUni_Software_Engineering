'''Write a program that receives three whole numbers and prints the largest one.'''

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)
