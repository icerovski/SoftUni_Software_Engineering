'''
Write a program that keeps the information about companies and their employees. 
You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company.
Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
Input / Constraints
•	Until you receive the "End" command, you will be receiving input in the format: 
"{company_name} -> {employee_id}".
•	The input always will be valid.
'''

def update_dictionary(company, employee):
    if company not in dictionary:
        dictionary[company] = []
    if employee not in dictionary[company]:
        dictionary[company].append(employee)

dictionary = {}
while True:
    input_str = input()
    if input_str == 'End':
        break
    elements = input_str.split(' -> ')
    company = elements[0]
    employee_id = elements[1]

    update_dictionary(company, employee_id)

for company, employees in dictionary.items():
    print(f'{company}')
    print('\n'.join(['-- ' + el for el in employees]))
