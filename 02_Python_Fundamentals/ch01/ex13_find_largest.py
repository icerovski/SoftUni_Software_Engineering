'''
You will be given a number. Print the largest number
that can be formed from the digits of the given number.
'''

NUM = int(input())
num_array = list(str(NUM))
n = len(num_array)

for i in range(n):
    # Create a flag that will allow the code to
    # terminate early if there's nothing left to sort
    already_sorted = True

    # Start looking at each item of the list one by one,
    # comparing it with its adjacent value. With each
    # iteration, the portion of the array that you look at
    # shrinks because the remaining items have already been
    # sorted.
    for j in range(n - i - 1):
        if num_array[j] < num_array[j + 1]:
            # If the item you're looking at is greater than its
            # adjecent value, then swap them
            num_array[j], num_array[j + 1] = num_array[j + 1], num_array[j]
            
            # Since you had to swap two elements,
            # set the 'already_sorted' flag to 'False' so the
            # algorithm doesn't finish prematurely
            already_sorted = False

    # If there were no swaps during the last iteration,
    # the array is already sorted, and you can terminate
    if already_sorted:
        break

print(int(''.join(num_array)))
