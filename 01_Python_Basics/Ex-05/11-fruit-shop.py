fruit = input()
day = input()
quantity = float(input())

fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

if fruit not in fruits:
    print('error')

else:
    if day not in workdays + weekend:
        print('error')
    else:
        i = fruits.index(fruit)
        
        if day in workdays:
            price = [2.5, 1.2, 0.85, 1.45, 2.7, 5.5, 3.85][i]
        elif day in weekend:
            price = [2.7, 1.25, 0.9, 1.6, 3, 5.6, 4.2][i]
        print(f'{quantity * price:.2f}')