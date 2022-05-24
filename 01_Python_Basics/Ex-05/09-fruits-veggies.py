product = input()

fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
veggies = ['tomato', 'cucumber', 'pepper', 'carrot']

if product in fruits: print('fruit')
elif product in veggies: print('vegetable')
else: print('unknown')