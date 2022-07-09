'''
You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}".
On the last line, you will receive a name of a course in snake case lowercase letters.
You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines. 
'''

def adjust_string(strng):
    return ' '.join(strng.split('_'))

def update_nested_dict(nested, master):
    if nested not in master:
        master[nested] = {}


course_journal = {}
while True:
    command = input()
    if ':' not in command:
        break

    parts = command.split(':')
    name = parts[0]
    ID = parts[1]
    course = parts[2]

    update_nested_dict(course, course_journal)
    course_journal[course][name] = ID

current_course = course_journal[adjust_string(command)]
for k, v in current_course.items():
    print(f'{k} - {v}')
