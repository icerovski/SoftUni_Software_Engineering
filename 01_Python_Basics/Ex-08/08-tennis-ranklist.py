tournaments_count = int(input())
points_initial = int(input())
points_addition = 0
w_count = 0

for i in range(0, tournaments_count):
    stage = input()
    if stage == 'W': 
        points_addition += 2000
        w_count += 1
    elif stage == 'F': points_addition += 1200
    elif stage == 'SF': points_addition += 720

points_final = points_initial + points_addition
avg_points = points_addition // tournaments_count
win_pct = w_count / tournaments_count * 100

print(f'Final points: {points_final}')
print(f'Average points: {avg_points}')
print(f'{win_pct:.2f}%')