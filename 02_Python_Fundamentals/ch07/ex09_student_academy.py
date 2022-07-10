'''
Write a program that keeps the information about students and their grades. 
On the first line, you will receive an integer number representing the next pair of rows.
On the next lines, you will be receiving each student's name and their grade. 
Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.
'''


def avg_grade(lst):
    return sum(lst) / len(lst)

def update_dictionary(student, grade):
    if student not in dictionary:
        dictionary[student] = {'grades' : [], 'avg_grade': 0}
    dictionary[student]['grades'].append(grade)
    dictionary[student]['avg_grade'] = avg_grade(dictionary[student]['grades'])

dictionary = {}
count = int(input())
for _ in range(count):
    student = input()
    grade = float(input())
    update_dictionary(student, grade)

# filter dictionary - remove the key if one of its items is greater than 4.5
# how to do it with dictionary comprehension
filtered = dict(filter(lambda item: item[1]['avg_grade'] >= 4.5, dictionary.items()))
for student, grades in filtered.items():
    print(f"{student} -> {grades['avg_grade']:.2f}")
