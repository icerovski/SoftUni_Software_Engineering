city = input()
sales = float(input())

cities = ['Sofia', 'Varna', 'Plovdiv']

if sales < 0 or city not in cities:
    print('error')
else:
    i = cities.index(city)
    
    # if sales >= 0 and sales <= 500:
    #     comish = sales * [0.05, 0.045, 0.055][i]
    # elif sales > 500 and sales <= 1000:
    #     comish = sales * [0.07, 0.075, 0.08][i]
    # elif sales > 1000 and sales <= 10000:
    #     comish = sales * [0.08, 0.1, 0.12][i]
    # elif sales > 10000:
    #     comish = sales * [0.12, 0.13, 0.145][i]

    if 0 <= sales <= 500:
        comish = sales * [0.05, 0.045, 0.055][i]
    elif 500 < sales <= 1000:
        comish = sales * [0.07, 0.075, 0.08][i]
    elif 1000 < sales <= 10000:
        comish = sales * [0.08, 0.1, 0.12][i]
    elif sales > 10000:
        comish = sales * [0.12, 0.13, 0.145][i]

    print(f'{comish:.2f}')    