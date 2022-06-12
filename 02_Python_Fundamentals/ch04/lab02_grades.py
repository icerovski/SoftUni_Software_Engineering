'''
Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
•	2.00 – 2.99 - "Fail"
•	3.00 – 3.49 - "Poor"
•	3.50 – 4.49 - "Good"
•	4.50 – 5.49 - "Very Good"
•	5.50 – 6.00 - "Excellent"
'''

def convert_grade(grd):
    grd_word = ''
    if 2 <= grd <= 2.99:
        grd_word = 'Fail'
    if 3 <= grd <= 3.49:
        grd_word = 'Poor'
    if 3.5 <= grd <= 4.49:
        grd_word = 'Good'
    if 4.5 <= grd <= 5.49:
        grd_word = 'Very Good'
    if 5.5 <= grd <= 6:
        grd_word = 'Excellent'
    print(grd_word)

grade = float(input())
convert_grade(grade)