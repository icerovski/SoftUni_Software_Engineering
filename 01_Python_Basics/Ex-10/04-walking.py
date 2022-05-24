steps_target = 10000
steps_total = 0
reached_goal = False

while steps_total < steps_target:
    current_action = input()
    if current_action == 'Going home':
        current_action = int(input())
        steps_total += current_action
        if steps_total >= steps_target: 
            reached_goal = True
        break
    else:
        steps_total += int(current_action)
        if steps_total >= steps_target:
            reached_goal = True
            break

steps_difference = abs(steps_target - steps_total)
if reached_goal:
    print('Goal reached! Good job!')
    print(f'{steps_difference} steps over the goal!')
else:
    print(f'{steps_difference} more steps to reach goal.')