'''
Write a function that receives a string and a counter n.
The function should return a new string – the result of repeating the old string n times.
Print the result of the function. Try using lambda.
'''
str_input = input()
counter = int(input())
repeat_string = lambda x, y: x * y
result = repeat_string(str_input, counter)
print(result)