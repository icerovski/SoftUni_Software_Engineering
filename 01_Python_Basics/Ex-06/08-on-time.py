exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrive_hour * 60 + arrive_minute

comp_time = exam_time - arrival_time
comp_hours = abs(comp_time) // 60 # if comp_time is negative and less than 60, the result will be -1 instead of 0, so use absolute number
comp_minutes = abs(comp_time) % 60

def seconds(s):
    if s < 10: return '0' + str(s)
    else: return s

if comp_time < 0:
    print('Late')
    if comp_hours == 0:
        print(f'{comp_minutes} minutes after the start')
    else:
        print(f'{comp_hours}:{seconds(comp_minutes)} hours after the start')

elif 0 <= comp_time <= 30:
    print('On time')
    if comp_time != 0:
        print(f'{comp_minutes} minutes before the start')

elif comp_time > 30:
    print('Early')
    if comp_hours == 0:
        print(f'{comp_minutes} minutes before the start')
    else:
        print(f'{comp_hours}:{seconds(comp_minutes)} hours before the start')
