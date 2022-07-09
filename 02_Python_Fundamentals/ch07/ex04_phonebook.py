'''
Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". 
If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N.
Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
In case the contact isn't found, print: "Contact {name} does not exist."
'''


tel_book = {}
while True:
    entry = input().split('-')
    if entry[0].isnumeric():
        num = int(entry[0])
        break
    tel_book[entry[0]] = entry[1]

for _ in range(num):
    name = input()
    if name not in tel_book.keys():
        print(f'Contact {name} does not exist.')
        continue
    print(f'{name} -> {tel_book[name]}')
