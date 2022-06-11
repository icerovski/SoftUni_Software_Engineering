'''
On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
You should create a list of courses and print it.
'''

input_n = int(input())
courses_list = []
while input_n > 0:
    courses_list.append(input())
    input_n -= 1

print(courses_list)
