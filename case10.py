
records = []
total_fine = 0

n = int(input("Enter number of books: "))

if n < 0:
    print("Invalid number of books")
else:
    valid = True

    for i in range(n):
        book_id = input("Enter book ID: ")
        days = int(input("Enter borrowing days: "))

        if days < 0:
            valid = False
        else:
            records.append((book_id, days))

    if not valid:
        print("Invalid borrowing duration")
    else:
        for book_id, days in records:
            overdue = max(0, days - 7)
            fine = overdue * 2
            total_fine += fine

            print("Book ID:", book_id)
            print("Overdue days:", overdue)
            print("Fine: Rs.", fine)

        print("Total fine: Rs.", total_fine)
