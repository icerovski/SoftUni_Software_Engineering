'''
Write a program that receives a single string containing positive and negative numbers separated by a single space.
Print a list containing the opposite of each number.
'''

# receive a string of numbers separated by space,
# split them into a list of strings with .split() and convert each item into integer with map()
num_list = map(int, input().split(' '))
opposite = list(map(lambda x: -1 * x, num_list))
print(opposite)
