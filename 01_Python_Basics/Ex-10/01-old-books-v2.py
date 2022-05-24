fav_book = input()

counter = 0

# Suggested by SoftUni
is_book_found = False 

current_book = input()
while current_book != 'No More Books':
    if current_book == fav_book:
        print(f'You checked {counter} books and you found it.')
        is_book_found = True
        break

    current_book = input()
    counter += 1

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')