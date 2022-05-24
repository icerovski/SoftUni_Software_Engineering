'''
Write a program that takes a single string and prints a list of all the capital letters indices.
'''

STR = input()
index_list = []
LEN = len(STR)

# start = 0
for i in range(0, LEN):
    if STR[i].isupper():
        index_list.append(i)

print(index_list)
