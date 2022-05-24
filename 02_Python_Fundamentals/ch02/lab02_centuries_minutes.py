'''
Write a program that reads an integer number of centuries and converts it to
years, days, hours, and minutes.
'''

centuries = int(input())
years_in_century = 100
days_in_year = 365.2422
hours_in_day = 24
minutes_in_hour = 60

years = centuries * years_in_century
days = int(years * days_in_year)
hours = days * hours_in_day
minutes = hours * minutes_in_hour

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
