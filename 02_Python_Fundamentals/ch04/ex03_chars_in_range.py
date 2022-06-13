'''
Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), separated by a single space. Print the result on the console.
'''

def return_string(a, b):
    start = ord(a)
    end = ord(b)
    new_string = ''
    for i in range(start + 1, end):
        new_string += chr(i) + ' '
    # removes the last character by slicing
    # https://www.pythonpool.com/python-remove-last-character-from-string/
    return new_string[:-1]

char_start = input()
char_end = input()

print(return_string(char_start, char_end))
