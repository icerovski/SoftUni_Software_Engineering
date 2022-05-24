n1 = int(input())
n2 = int(input())

for num in range(n1, n2 + 1):
    odd_sum = 0
    even_sum = 0
    count = len(str(num))
    
    print_num = num
    # loop through all digits of a number
    while num > 0:    
        digit = num % 10
        if count % 2 != 0:
            odd_sum += digit
        elif count % 2 == 0:
            even_sum += digit
        
        num = num // 10
        count -= 1

    if odd_sum == even_sum:
        print(print_num, end=' ')


# loop through digits of the number
# i = 12345
# while i > 0:
#     digit = i % 10
#     print(digit)
#     i = i // 10