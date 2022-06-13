'''
Write a function that receives three integer numbers and returns the smallest.
Print the result on the console. Use an appropriate name for the function.
'''

def smallest(one, two, three):
    sequence = [one, two, three]
    # return the first item in a sorted sequence
    return sorted(sequence)[0]

int_one = int(input())
int_two = int(input())
int_three = int(input())

print(smallest(int_one, int_two, int_three))
