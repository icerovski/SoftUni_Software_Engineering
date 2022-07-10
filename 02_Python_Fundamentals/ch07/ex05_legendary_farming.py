'''
You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
•	"Shadowmourne" - requires 250 Shards
•	"Valanyr" - requires 250 Fragments
•	"Dragonwrath" - requires 250 Motes
"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk. 
You will be given lines of input in the format: 
"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Keep track of the key materials - the first one that reaches 250, wins the race.
At that point, you have to print that the corresponding legendary item is obtained. 
In the end, print the remaining shards, fragments, motes in the format:
"shards: {number_of_shards}
fragments: {number_of_fragments}
motes: {number_of_motes}"
Finally, print the collected junk items in the order of appearance.

Input
•	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Output
•	On the first line, print the obtained item in the format: "{Legendary item} obtained!"
•	On the next three lines, print the remaining key materials 
•	On the several final lines, print the junk items
•	All materials should be printed in the format: "{material}: {quantity}"
•	The output should be lowercase, except for the first letter of the legendary
'''

def update_junk(name, qty):
    if name not in junk:
        junk[name] = 0
    junk[name] += qty

materials = {}
junk = {}
materials['shards'] = {'legendary' : 'Shadowmourne', 'quantity' : 0}
materials['fragments'] = {'legendary' : 'Valanyr', 'quantity' : 0}
materials['motes'] = {'legendary' : 'Dragonwrath', 'quantity' : 0}
winner_quantity = 250
have_winner = False

while True:
    input_lst = input().split(' ')
    for i in range(0, len(input_lst), 2):
        new_quantity = int(input_lst[i])
        material = input_lst[i+1].lower()
        if material not in materials:
            update_junk(material, new_quantity)
            continue
        
        current_quantity = materials[material]['quantity']
        materials[material]['quantity'] += new_quantity
        if materials[material]['quantity'] >= winner_quantity:
            materials[material]['quantity'] -= winner_quantity
            legendary_item = materials[material]['legendary']
            have_winner = True
            break
    
    if have_winner:
        break

print(f'{legendary_item} obtained!')
for k, v in materials.items():
    print(f'{k}: {v["quantity"]}')

for k, v in junk.items():
    print(f'{k}: {v}')
