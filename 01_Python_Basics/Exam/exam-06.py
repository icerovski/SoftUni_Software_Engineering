k = int(input())
l = int(input())
m = int(input())
n = int(input())

subs = 6
no_more_subs = False
for i in range(k, 8 + 1):
    for j in range(9, l - 1, -1):
        for x in range(m, 8 + 1):
            for y in range(9, n - 1, -1):
                if i % 2 == 0 and j % 2 != 0 and x % 2 == 0 and y % 2 != 0:
                    if (10 * i + j) != (10 * x + y):
                        print(f'{i}{j} - {x}{y}')
                        subs -= 1
                        if subs == 0:
                            no_more_subs = True
                            break
                    else:
                        print('Cannot change the same player.')
            
            if no_more_subs: break

        if no_more_subs: break
    
    if no_more_subs: break
