'''
Write a program that receives a single string (integers separated by a comma and space ", "),
finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.
'''
int_list = list(map(int, input().split(', ')))
filtered = list(filter(lambda x: x != 0, int_list))
zeros_count = len(int_list) - len(filtered)

# Initialize a list with any size and values
# list = [0, 1, 2] * 3
for _ in range(zeros_count):
    filtered.append(0)

print(filtered)
