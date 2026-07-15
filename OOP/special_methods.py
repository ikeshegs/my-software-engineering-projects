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
print(item1 < item2)  # Output: True
