class BankAccount:      # class

    bank_name = "ABC Bank"          # class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner          # attributes
        self.__balance = balance    # attributes (private method (Encapsulation))

    def deposit(self, amount):      # deposit & withdraw are methods
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)    # account is an object

account.deposit(500)
account.withdraw(200)

# print(account.get_balance())

# Create a Book class with title, author, and price attributes. Add a method to display the book's details.
class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price
        
    def display_book(self):
        return f"'{self.title}' authored by '{self.author}' is selling for N{self.price:.2f}."

book1 = Book("Things Fall Apart", "Chinua Achiebe", 2500.00)

# print(book1.display_book())

# Create a Rectangle class with width and height attributes. Implement methods to calculate its area and perimeter.
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return f"The area of the rectangle is {self.width * self.height}"
    
    def calculate_perimater(self):
        return f"The perimeter of the rectangle is {2 * (self.width + self.height)}"
    
rectangle1 = Rectangle(15, 38)

# print(rectangle1.calculate_area())
# print(rectangle1.calculate_perimater())

# Create a Vehicle class and derive Car and Motorcycle classes that override a start() method.
class Vehicle:
    def __init__(self):
        pass
    
    def start(self):
        return "Starting the Vehicle...."
        
class Car(Vehicle):
    def start(self):
        return "Car is starting...."
        
class Motorcycle(Vehicle):
    def start(self):
        return "Motorcycle is starting...."

car = Car()
# print(car.start())

motorcycle = Motorcycle()
# print(motorcycle.start())

# Build a ShoppingCart class that allows adding, removing, and listing items, and calculating the total price.
class ShoppingCart:
    # shopping_list = []
    
    def __init__(self, shopping_list: list):
        self.__shopping_list = shopping_list
        
    def add_item(self, item: str, quantity: int, price: float):
        # self.item = item
        # self.quantity = quantity
        # self.price = price
        
        self.__shopping_list.append({
            "name": item,
            "quantity": quantity,
            "price": price
        })
        
    def list_cart_items(self):
        return self.__shopping_list
    
    def remove_item(self, item_index: int):
        # self.item_index = item_index
        
        # if self.item_index < len(self.__shopping_list):
        #     for item in self.__shopping_list:
        #         if self.item_index == self.__shopping_list.index(item):
        #             return self.__shopping_list.remove(item)
        # else:
        #     raise IndexError("Number is greater than length of the list.")
        
        if not 0 <= item_index < len(self.__shopping_list):
            raise IndexError("Index out of range")
        
        self.__shopping_list.pop(item_index)
        
    def calculate_total(self):
        total = 0
        
        # for item in self.__shopping_list:
        #     for key, value in item.items():
        #         if key == "total item price":
        #             total += value
        
        # for item in self.__shopping_list:
        #     total += item["total item price"]
        
        # return total
        return sum((item["price"] * item["quantity"]) for item in self.__shopping_list)
    
shoppingcart = ShoppingCart([])

shoppingcart.add_item("PS5", 1, 3500)
shoppingcart.add_item("iPhone 17 Pro Max", 4, 1500)
shoppingcart.add_item("MacBook Pro Max M5 2026", 2, 4500)

print(shoppingcart.remove_item(2))
print(shoppingcart.list_cart_items())
print(shoppingcart.calculate_total())
