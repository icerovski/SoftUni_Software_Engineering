'''
You will be given two strings. Transform the first string into the second one,
letter by letter, starting from the first one. After each interaction,
print the resulting string only if it is unique.
Note: the strings will have the same length.
'''

STR_A = input()
STR_B = input()
LIST_A = list(STR_A)
last_str = STR_A
STR_LEN = len(STR_A)

for i in range(0, STR_LEN):
    CH_A = STR_A[i]
    CH_B = STR_B[i]
    if CH_A != CH_B:
        # STR_A = STR_A.replace(CH_A, CH_B, 1)
        LIST_A[i] = CH_B
        print(''.join(LIST_A))

# for i in range(STR_LEN):
#     left_part = STR_B[:i + 1]
#     right_part = STR_A[i + 1:]
#     current_str = left_part + right_part
#     if current_str == last_str:
#         continue
#     print(current_str)
#     last_str = current_str
