'''Write a program that receives a single word, reverses it, and prints it.'''
word = input()
REVERSED_WORD = ''

for i in range(len(word) - 1, -1, -1):
    REVERSED_WORD += word[i]

print(REVERSED_WORD)
