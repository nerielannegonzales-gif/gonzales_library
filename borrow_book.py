from add_book import books

loans = []

def borrow_book():

    if not books:
        print("No books available.")
        return

    print("\nAVAILABLE BOOKS")

    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']}")

    choice = int(input("Choose book number: "))

    if 1 <= choice <= len(books):

        borrowed = books.pop(choice - 1)

        loans.append(borrowed)

        print("Book borrowed successfully!")

    else:
        print("Invalid choice.")
