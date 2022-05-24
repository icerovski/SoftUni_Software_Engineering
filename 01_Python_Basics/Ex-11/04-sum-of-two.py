start = int(input())
end = int(input())
magic_num = int(input())

combination_count = 0
magic_combination = 0
magic_i = 0
magic_j = 0

combination_exists = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combination_count += 1
        
        if i + j == magic_num:
            magic_combination = combination_count
            magic_i = i
            magic_j = j
            combination_exists = True
            break
    
    if combination_exists: break

if combination_exists:
    print(f'Combination N:{magic_combination} ({magic_i} + {magic_j} = {magic_num})')
else:
    print(f'{combination_count} combinations - neither equals {magic_num}')
