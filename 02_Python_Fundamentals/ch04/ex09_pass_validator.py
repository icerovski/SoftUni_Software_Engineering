'''
Write a function that checks if a given password is valid. Password validations are:
•	It should be 6 - 10 (inclusive) characters long
•	It should consist only of letters and digits
•	It should have at least 2 digits 
If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:
•	"Password must be between 6 and 10 characters"
•	"Password must consist only of letters and digits"
•	"Password must have at least 2 digits"
'''


def check_length(strng):
    if 6 <= len(strng) < 11:
        return True
    print('Password must be between 6 and 10 characters')
    return False

def check_characters(strng):
    if strng.isalnum():
        return True
    print('Password must consist only of letters and digits')
    return False
    # for char in strng:
    #     # if not char.isdigit() or char.isalpha():
    #     if not char.isalnum()
    #         return False
    # return True

def check_digits_count(strng):
    digit_count = 0
    for char in strng:
        if char.isdigit():
            digit_count += 1
    if digit_count >= 2:
        return True
    print('Password must have at least 2 digits')
    return False


password = input()
validated = [
    check_length(password),
    check_characters(password),
    check_digits_count(password),
]
if all(validated):
    print('Password is valid')
