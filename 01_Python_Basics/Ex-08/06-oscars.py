name_actor = input()
points_initial = float(input())
judges_count = int(input())

points_for_oscar = 1250.5

while judges_count > 0:
    name_judge = input()
    points_by_judge = float(input())
    
    points_initial += len(name_judge) * points_by_judge / 2
    
    if points_initial >= points_for_oscar: break
    
    judges_count -= 1

if points_initial >= points_for_oscar:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {points_initial:.1f}!')
else:
    difference = points_for_oscar - points_initial
    print(f'Sorry, {name_actor} you need {difference:.1f} more!')