'''On the first line, you will be given a positive number, which will serve as a divisor.
On the second line, you will receive a positive number that will be the boundary.
You should find the largest integer N, that is:

•	divisible by the given divisor
•	less than or equal to the given bound
•	greater than 0

Note: it is guaranteed that N is found.'''

DIVISOR = int(input())
BOUNDARY = int(input())
N = 1
LARGEST_N = 0

while 0 < N <= BOUNDARY:
    if N % DIVISOR == 0:
        if LARGEST_N <= N:
            LARGEST_N = N
    N += 1

print(LARGEST_N)
