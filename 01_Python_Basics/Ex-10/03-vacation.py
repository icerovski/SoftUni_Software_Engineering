budget = float(input())
savings = float(input())

days_counter_spending = 0 # consecutive days that she spends instead of saves
days_counter = 0
reached_budget = False

while savings < budget:
    action = input()
    amount = float(input())
    days_counter += 1
    
    if action == 'spend':
        days_counter_spending += 1
        if days_counter_spending == 5: 
            break
    
        if savings < amount: 
            savings = 0 # if spending more than savings, use zero
        else: 
            savings -= amount
        
    if action == 'save':
        days_counter_spending = 0
        
        if savings + amount >= budget:
            reached_budget = True
            break
        else: savings += amount

if reached_budget:
    print(f'You saved the money for {days_counter} days.')
else:
    print("You can't save the money.")
    print(f"{days_counter}")