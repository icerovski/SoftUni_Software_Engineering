'''
On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings.
You should add them to a list and print them. After that, you should filter out only the strings that include the given word and print that list too.
'''
num_input = int(input())
key_word = input()
word_list = []

while num_input > 0:
    word_list.append(input())
    num_input -= 1
print(word_list)

filtered = []
filtered = list(filter(lambda word: key_word in word, word_list))
print(filtered)
