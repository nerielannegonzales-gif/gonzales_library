from add_book import add_book
from view_books import view_books
from register_member import register_member
from view_members import view_members
from borrow_book import borrow_book
from return_book import return_book
from view_loans import view_loans

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Register Member")
    print("4. View Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. View Loans")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        register_member()

    elif choice == "4":
        view_members()

    elif choice == "5":
        borrow_book()

    elif choice == "6":
        return_book()

    elif choice == "7":
        view_loans()

    elif choice == "8":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice.")
