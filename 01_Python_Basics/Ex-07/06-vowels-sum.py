input_text = input()

chars = ['a', 'e', 'i', 'o', 'u']
values = [1, 2, 3, 4, 5]

result = 0

for char in input_text:
    if char in chars:
        result = result + values[chars.index(char)]

print(result)