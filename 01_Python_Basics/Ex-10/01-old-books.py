fav_book = input()
book_name = input()
count = 0

while True:
    if book_name == fav_book:
        print(f'You checked {count} books and found it.')
        break
    elif book_name == "No More Books":
        print('The book you search is not here!')
        print(f'You checked {count} books.')
        break
    else:
        book_name = input()
        count += 1