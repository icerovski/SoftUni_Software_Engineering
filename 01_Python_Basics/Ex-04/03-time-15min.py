hours = int(input())
minutes = int(input())

placeholder_m = minutes + 15

if placeholder_m > 59:
    if hours + 1 > 23:
        hours = 0
    else:
        hours += 1
    minutes = placeholder_m % 59 - 1
else:
    minutes = placeholder_m

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')