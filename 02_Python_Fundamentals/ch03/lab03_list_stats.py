'''
On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
•	One with all the positives (including 0) numbers
•	One with all the negatives numbers
Finally, print the following message: 
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"
'''

total_nums = int(input())
positives = []
negatives = []
while total_nums > 0:
    num_input = int(input())
    if num_input >= 0:
        positives.append(num_input)
    else:
        negatives.append(num_input)

    total_nums -= 1

count_positives = len(positives)
sum_of_negatives = sum(negatives)

print(positives)
print(negatives)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_of_negatives}')
