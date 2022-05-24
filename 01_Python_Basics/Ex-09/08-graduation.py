name = input()

min_gpa = 4
school_years = 12

year_count = 1
grade_sum = 0
fail_count = 0

while year_count <= school_years:
    grade = float(input())
    if grade < min_gpa: 
        fail_count += 1
        if fail_count >= 2:
            print(f'{name} has been excluded at {year_count} grade')
            break
        else: continue
    
    grade_sum += grade
    if year_count == school_years:
        gpa = grade_sum / year_count
        print(f'{name} graduated. Average grade: {gpa:.2f}')
        break
    
    year_count += 1