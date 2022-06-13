'''
Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a sorted list of numbers in ascending order. Use sorted().
'''

def bubble_sort(array):
    n = len(array)
    # We push the LARGEST number to the END during the FIRSTiterration of 'i'
    for i in range(n):
        already_sorted = True

        # We push the SMALLEST number to the BEGINNING by the LAST iterration of 'j'
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


numbers = list(map(int, input().split(' ')))
print(bubble_sort(numbers))