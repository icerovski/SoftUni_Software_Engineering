n = int(input())
name = input()

count = 0
cum_avg_score = 0
while name != 'Finish':
    sum_score = 0
    for i in range(0, n):
        score = float(input())
        sum_score += score
    
    avg_score = sum_score / n
    print(f'{name} - {avg_score:.2f}.')

    cum_avg_score += avg_score
    count += 1

    name = input()

print(f"Student's final assessment is {cum_avg_score / count:.2f}.")