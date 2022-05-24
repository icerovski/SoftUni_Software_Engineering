n = int(input())

if n < 1 or n > 7:
    print('Error')
else:
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(week[n - 1])