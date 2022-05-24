'''
Write a program to read an integer N and print all triples of the first N small Latin letters,
ordered alphabetically.
'''

NUM = int(input())
ascii_first_latin_ch = 97

for i in range(NUM):
    for j in range(NUM):
        for k in range(NUM):
            print(f'{chr(ascii_first_latin_ch + i)}{chr(ascii_first_latin_ch + j)}{chr(ascii_first_latin_ch + k)}')
