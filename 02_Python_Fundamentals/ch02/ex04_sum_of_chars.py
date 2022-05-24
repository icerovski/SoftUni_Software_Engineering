'''
Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
On the first line, you will receive N – the number of lines.
On the following N lines – you will receive a letter per line.
Print the total sum in the following format: "The sum equals: {total_sum}".
Note: n will be in the interval [1…20].
'''

number_of_characters = int(input())
char_ASCII_sum = 0

while number_of_characters > 0:
    char_input = input()
    # To get the ASCII code of a character, use the ord() function.
    ascii_code_of_char = ord(char_input)
    char_ASCII_sum += ascii_code_of_char
    number_of_characters -= 1

print(f'The sum equals: {char_ASCII_sum}')
