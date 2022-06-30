'''
Create a class Class. The __init__ method should receive the name of the class. Each class should also have 2
empty lists - students and grades. Create a class attribute __students_count equal to 22. The class should
also have 3 additional methods:
• add_student(name: str, grade: float) - adds the student and the grade in the two lists if there is
free space in the class
• get_average_grade() - returns the average of all existing grades formatted to the second decimal point
(as a number)
• __repr__ - returns the string (single line):
"The students in {class_name}: {students}. Average grade: {average_grade}".
The students must be separated by a comma and a space: ", ".
'''

class Class:
    students = []
    grades = []
    __students_count = 22

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if len(Class.students) < Class.__students_count:
            Class.students.append(name)
            Class.grades.append(grade)

    def get_average_grade(self):
        return sum(Class.grades) / len(Class.grades)
    
    def format_lst(self, lst):
        return ', '.join(lst)

    def __repr__(self):
        return f'The students in {self.name}: {self.format_lst(Class.students)}. Average grade: {self.get_average_grade():.2f}'


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
