destination = input()

top_up = 0
cum_savings = 0

while destination != 'End':
    budget = float(input())

    cum_savings = 0
    while cum_savings < budget:
        top_up = float(input())
        cum_savings += top_up

        if cum_savings >= budget:
            print(f'Going to {destination}!')
            break
    
    destination = input()
