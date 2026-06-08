from borrow_book import loans
from add_book import books

def return_book():

    if not loans:
        print("No borrowed books.")
        return

    print("\nBORROWED BOOKS")

    for index, book in enumerate(loans, start=1):
        print(f"{index}. {book['title']}")

    choice = int(input("Choose book number to return: "))

    if 1 <= choice <= len(loans):

        returned = loans.pop(choice - 1)

        books.append(returned)

        print("Book returned successfully!")

    else:
        print("Invalid choice.")
