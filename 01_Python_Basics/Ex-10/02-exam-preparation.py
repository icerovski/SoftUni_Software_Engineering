# The number of failed marks before you take a break
fails_count_for_break = int(input())
fails_counter = 0
is_break_needed = False

# Receive this task in order to go into a break
task_name_for_break = 'Enough'
task_counter = 0

# Place holder for the sum of all scores
score_sum = 0

task_name = input()
previous_task_name = task_name
while task_name != task_name_for_break:
# After having checked if the name is 'Enough', receive the task score
    task_score = float(input())

# Check if task is fail
    if task_score <= 4:
        fails_counter += 1

# Check if the 'Enough' command is given
    if fails_counter == fails_count_for_break:
        print(f'You need a break, {fails_counter} poor grades.')
        is_break_needed = True
        break

# Compount the score
    score_sum += task_score

# Preserve the name of the previous task
    previous_task_name = task_name

# Get the next task name and task score
    task_name = input()
# Compound the number of tasks
    task_counter += 1


if not is_break_needed:
    avg_score = score_sum / task_counter
    print(f'Average score: {avg_score:.2f}')
    print(f'Number of problems: {task_counter}')
    print(f'Last problem: {previous_task_name}')
