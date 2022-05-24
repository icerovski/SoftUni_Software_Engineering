prime_sum = 0
nonprime_sum = 0

line = input()
while line != 'stop':
    num = int(line)
    if num > 1:
        # If num is divisible by any number between 
        # 2 and num // 2, it is not prime
        is_not_prime = False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_not_prime = True
                break
        
        if is_not_prime:
            nonprime_sum += num
        else:
            prime_sum += num
    elif num == 0 or num == 1:
        nonprime_sum += num
    elif num < 0:
        print('Number is negative.')
        
    line = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {nonprime_sum}')
