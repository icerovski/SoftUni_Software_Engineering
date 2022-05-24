total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie = input()
while movie != 'Finish':
    movie_capacity = int(input())
    ticket_count = 0
    ticket = input()
    while ticket != 'End':
        if ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'kid':
            kid_tickets += 1
        
        ticket_count += 1
        total_tickets += 1

        if ticket_count == movie_capacity:
            break
        else:
            ticket = input()
    
    movie_capacity_pct = ticket_count / movie_capacity * 100
    print(f'{movie} - {movie_capacity_pct:.2f}% full.')

    movie = input()

student_tickets_pct = student_tickets / total_tickets * 100
standard_tickets_pct = standard_tickets / total_tickets * 100
kid_tickets_pct = kid_tickets / total_tickets * 100

print(f'Total tickets: {total_tickets}')
print(f'{student_tickets_pct:.2f}% student tickets.')
print(f'{standard_tickets_pct:.2f}% standard tickets.')
print(f'{kid_tickets_pct:.2f}% kids tickets.')