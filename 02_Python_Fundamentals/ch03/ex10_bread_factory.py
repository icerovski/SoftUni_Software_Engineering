'''
As a young baker, you are baking the bread out of the bakery. 
You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
•	If the event is "rest":
o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.". 
o	After that, print your current energy: "Current energy: {current_energy}.".
•	If the event is "order": 
o	You've earned some coins (the number in the second part). 
o	Each time you get an order, your energy decreases by 30 points.
	If you have the energy to complete the order, print: "You earned {earned} coins.".
	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
•	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend. 
o	If you have enough money, you should buy the ingredient and print:
"You bought {ingredient}."
o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 
If you managed to handle all events through the day, print on the following 3 lines: 
"Day completed!"
"Coins: {coins}"
"Energy: {energy}"
Input / Constraints
You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
"event1|event2| … eventN".
Each event contains an event name or an ingredient and a number, separated by a dash in the format: "{event/ingredient}-{number}"
Output
Print the corresponding messages described above.
'''
list_of_events = input().split('|')
energy = 100
coins = 100
bakery_is_open = True
for event in list_of_events:
    current_event = event.split('-')
    current_event_action = current_event[0]
    number = int(current_event[1])

    if current_event_action == 'rest':
        gained_energy = min(number, 100 - energy)
        energy += gained_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif current_event_action == 'order':
        if energy < 30:
            energy += min(50, 100 - energy)
            print('You had to rest!')
            continue
        energy -= 30
        coins += number
        print(f'You earned {number} coins.')
    else:
        if coins < number:
            print(f'Closed! Cannot afford {current_event_action}.')
            bakery_is_open = False
            break
        coins -= number
        print(f'You bought {current_event_action}.')

if bakery_is_open:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
