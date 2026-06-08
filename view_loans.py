from borrow_book import loans

def view_loans():

    if not loans:
        print("No borrowed books.")
        return

    print("\nBORROWED BOOKS")

    for index, book in enumerate(loans, start=1):
        print(f"{index}. {book['title']}")
