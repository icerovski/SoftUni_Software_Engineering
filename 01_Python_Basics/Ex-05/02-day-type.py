day = input()
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

if day in workdays: print('Working day')
elif day in weekend: print('Weekend')
else: print('Error')