from add_book import books

def view_books():

    if not books:
        print("No books available.")
        return

    print("\nBOOK LIST")

    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']} by {book['author']}")
