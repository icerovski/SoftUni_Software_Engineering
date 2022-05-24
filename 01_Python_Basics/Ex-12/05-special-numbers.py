numerator = int(input())

for num in range(1111, 9999 + 1):
    is_magic = True
    magic_number = num

    # loop through digits of a number, 
    # starting from right to left, trimming the original number
    # down to zero, where you exit the loop
    while num > 0:
        # take the right most digit
        digit = num % 10
        # permanently trim the number from that right most digit
        num = num // 10
        # perform desired analysis of the digit before looping
        # back to the begining
        if digit == 0 or numerator % digit != 0:
            is_magic = False
            break
    
    if is_magic: 
        print(f'{magic_number}', end=' ')