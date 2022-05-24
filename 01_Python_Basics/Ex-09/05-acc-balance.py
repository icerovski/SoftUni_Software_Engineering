deposit = input()
sum = 0
while deposit != 'NoMoreMoney':
    deposit_num = float(deposit)

    if deposit_num < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {deposit_num:.2f}')
    sum += deposit_num
    deposit = input()

print(f'Total: {sum:.2f}')