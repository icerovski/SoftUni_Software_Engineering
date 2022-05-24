'''
Write a program that prints part of the ASCII table characters on the console,
separated by a single space. On the first line of input, you will receive the char index
you should start with. On the second line - the index of the last character you should print. 
'''

start_index = int(input())
end_index = int(input())
separator = ' '

for i in range(start_index, end_index + 1):
    # To get the character encoded by an ASCII code number, use the chr() function.
    ascii_symbol = chr(i)
    print(ascii_symbol, end=separator)
