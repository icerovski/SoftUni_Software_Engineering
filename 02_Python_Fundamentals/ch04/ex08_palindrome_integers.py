'''
A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
Write a function that receives a list of positive integers, separated by comma and space ", ".
The function should check if each integer is a palindrome - True or False. Print the result.
'''

def palindrome_check(strng):
    mid = len(strng) // 2
    left_strng = strng[:mid]
    right_strng = strng[mid:]
    for i in range(mid):
        if left_strng[i] != right_strng[-i - 1]:
            return False
    return True

sequence = input().split(', ')
for item in sequence:
    print(palindrome_check(item))
