# The two classes created below, can exist independently without the other, but in Aggregation the Library class referenced the Book class.
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        
library = Library("Abuja International Library")

book1 = Book("Harry Potter", "J.K. Rowlings")
book2 = Book("Acheron", "Sherrilyn Kenyon")
book3 = Book("Things Fall Apart", "Chinua Achiebe")

library.add_book(book1)     # Aggregation
library.add_book(book2)     # Aggregation
library.add_book(book3)     # Aggregation

print(library.name)

for book in library.list_books():
    print(book)
