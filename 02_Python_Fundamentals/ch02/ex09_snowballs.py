'''
Tony and Andi love playing in the snow and having snowball fights, but they always argue about which makes the best snowballs.
They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.
You will receive N – an integer, the number of snowballs being made by Tony and Andi.
On the following lines, you will receive 3 inputs for each snowball:
•	The weight of the snowball (integer).
•	The time needed for the snowball to get to its target (integer).
•	The quality of the snowball (integer).
For each snowball, you must calculate its value by the following formula:
(snowball_weight / snowball_time) ** snowball_quality
In the end, you must print the highest calculated value of a snowball.
Input
•	On the first input line, you will receive N – the number of snowballs.
•	On the next N*3 input lines, you will be receiving data about each snowball. 
Output
•	You need to print the highest calculated snowball's value in the format: 
"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
Constraints
•	The number of snowballs (N) will be an integer in range [0, 100].
•	The weight is an integer in the range [0, 1000].
•	The time is an integer in the range [1, 500].
•	The quality is an integer in the range [0, 100].
'''

NUM = int(input())
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0

while NUM > 0:
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())

    current_snowball_value = int((current_snowball_weight / current_snowball_time) ** current_snowball_quality)

    if current_snowball_value > snowball_value:
        snowball_weight = current_snowball_weight
        snowball_time = current_snowball_time
        snowball_quality = current_snowball_quality
        snowball_value = current_snowball_value

    NUM -= 1

print(f'{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})')
