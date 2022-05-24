'''
Wolf in Sheep's Clothing

Uslovieto is rediculous, so I'm not gonna type it here

[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   4      3            2      1
'''

INPUT_STR = input()
input_list = INPUT_STR.split(', ')
LEN = len(input_list)

for i in range(LEN):
    if input_list[i] == 'wolf':
        # Since you are "standing" in front of the last member of the list
        # Your perspective will be reverse to the normal list logic
        WOLF_INDEX = LEN - i
        break

if WOLF_INDEX == 1:
    print('Please go away and stop eating my sheep')
else:
    SHEEP_INDEX = WOLF_INDEX - 1
    print(f'Oi! Sheep number {SHEEP_INDEX}! You are about to be eaten by a wolf!')
