'''
You will receive two lines of input: 
•	a list of employees' happiness as a string of numbers separated by a single space 
•	a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office. 
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
•	If half or more of the employees have happiness greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
•	Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
'''

from functools import reduce

employee_happiness = list(map(int, input().split(' ')))
factor = int(input())

factored = list(map(lambda x: x * factor, employee_happiness))
total_employees = len(factored)
avg_happiness = reduce(lambda x, y: x + y, factored) / total_employees
filtered = list(filter(lambda x: x >= avg_happiness, factored))
happy_employees = len(filtered)
if happy_employees >= total_employees // 2:
    print(f"Score: {happy_employees}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{total_employees}. Employees are not happy!")
