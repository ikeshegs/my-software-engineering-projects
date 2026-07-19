# Object Lifecycle (Initialization & Representation)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("1984", "George Orwell")
# print(str(book))   # Output: '1984' by George Orwell
# print(repr(book))  # Output: Book(title='1984', author='George Orwell')

# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines behavior for addition (+)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
# print(p1 + p2)  # Output: Point(4, 6)

# Comparison Operators
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Defines behavior for less-than (<)
    def __lt__(self, other):
        return self.price < other.price

item1 = Product("Mouse", 25)
item2 = Product("Keyboard", 75)
# print(item1 < item2)  # Output: True

#
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}'s account has ${self.balance}"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

account = BankAccount("Alice", 3450)

# print(account)      # print() uses __str__

# A List of Objects
accounts = [
    BankAccount("Alice", 2500),
    BankAccount("Bob", 1800)
]
# print(accounts)     # Here print() uses the __repr__

# __getitem__ example 1
class Student:
    def __init__(self):
        self.grades = {
            "Math": 95,
            "English": 88,
            "Science": 91
        }

    def __getitem__(self, subject):
        return self.grades[subject]

student = Student()

# print(student["Math"])
# print(student["Science"])

# __getitem__ example 2
class Playlist:
    def __init__(self):
        self.songs = [
            "Blinding Lights",
            "Shape of You",
            "Believer"
        ]

    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist()

# print(playlist[0])
# print(playlist[2])

# __getitem__ example 3
class Library:
    def __init__(self):
        self.books = [
            "Python Basics",
            "Clean Code",
            "Algorithms"
        ]

    def __getitem__(self, index):
        return self.books[index]

library = Library()

# print(library[1])

# __getitem__ example 4
class Store:
    def __init__(self):
        self.products = {
            101: "Laptop",
            102: "Phone",
            103: "Keyboard"
        }

    def __getitem__(self, product_id):
        return self.products[product_id]

store = Store()

# print(store[102])

# __getitem__ example 5
class Point:
    def __init__(self, x, y):
        self.coordinates = (x, y)

    def __getitem__(self, index):
        return self.coordinates[index]

point = Point(10, 20)

# print(point[0])
# print(point[1])
