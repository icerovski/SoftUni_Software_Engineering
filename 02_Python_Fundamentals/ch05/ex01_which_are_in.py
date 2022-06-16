'''
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.
'''

import timeit

substring_list = input().split(', ')
main_list = input().split(', ')

def result_comprehension():
    new_list = []
    for sub_word in substring_list:
        new_list += [sub_word for word in main_list if word.find(sub_word) != -1]
    return new_list
    # return list(sorted(set(new_list)))

def result_loop():
    new_list = []
    for sub_word in substring_list:
        for word in main_list:
            if word.find(sub_word) != -1:
                new_list.append(sub_word)
                break
    return new_list

print(result_comprehension())
print(result_loop())
print(timeit.timeit(result_comprehension))
print(timeit.timeit(result_loop))
