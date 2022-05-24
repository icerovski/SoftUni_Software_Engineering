groups_count = int(input())
all_people = 0
musala = 0
monblan = 0
kali = 0
k2 = 0
everest = 0

for i in range(0, groups_count):
    people_count = int(input())
    all_people += people_count
    
    if people_count <= 5: musala += people_count
    elif 5 < people_count <= 12: monblan += people_count
    elif 12 < people_count <= 25: kali += people_count
    elif 25 < people_count <= 40: k2 += people_count
    else: everest += people_count

factor = 100 / all_people
print(f'{musala * factor :.2f}%')
print(f'{monblan * factor:.2f}%')
print(f'{kali * factor:.2f}%')
print(f'{k2 * factor:.2f}%')
print(f'{everest * factor:.2f}%')