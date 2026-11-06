# This is my second project on my AI Software Engineering Study Plan. The project is a library management system that allows users to manage books, members, and borrowing records. The system provides functionalities for adding, updating, and deleting books and members, as well as tracking borrowed books.

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = {}

    def add_book(self, book):
        """Add a new book to the library."""
        self.books.append(book)
        
    def get_all_books(self):
        """Get a list of all books in the library."""
        for index, book in enumerate(self.books, start=1):
            print(f"{index}: {book}")

    def remove_book(self, book):
        """Remove a book from the library."""
        if book in self.books:
            self.books.remove(book)

    def add_member(self, member):
        """Add a new member to the library."""
        self.members.append(member)

    def remove_member(self, member):
        """Remove a member from the library."""
        if member in self.members:
            self.members.remove(member)

    def borrow_book(self, member, book):
        """Allow a member to borrow a book."""
        if book in self.books and member in self.members:
            self.borrowed_books[book] = member
            self.books.remove(book)

    def return_book(self, book):
        """Allow a member to return a borrowed book."""
        if book in self.borrowed_books:
            del self.borrowed_books[book]
            self.books.append(book)

library = Library()

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Add Member")
        print("5. Remove Member")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book = input("Enter book title: ")
            library.add_book(book)
            print(f"Book '{book}' added to the library.")
        elif choice == '2':
            book = input("Enter book title to remove: ")
            library.remove_book(book)
            print(f"Book '{book}' removed from the library.")
        elif choice == '3':
            library.get_all_books()
        elif choice == '4':
            member = input("Enter member name: ")
            library.add_member(member)
            print(f"Member '{member}' added to the library.")
        elif choice == '5':
            member = input("Enter member name to remove: ")
            library.remove_member(member)
            print(f"Member '{member}' removed from the library.")
        elif choice == '6':
            member = input("Enter member name: ")
            book = input("Enter book title to borrow: ")
            library.borrow_book(member, book)
            print(f"Member '{member}' borrowed book '{book}'.")
        elif choice == '7':
            book = input("Enter book title to return: ")
            library.return_book(book)
            print(f"Book '{book}' returned to the library.")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

main()
