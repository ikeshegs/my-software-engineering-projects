from abc import ABC, abstractmethod

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
    def __init__(self, name):
        self.name = name
        self.__shopping_list = []
        
    def add_cart_item(self, cart_item):
        self.__shopping_list.append(cart_item)
        
    def list_cart_items(self):
        # return [f"{cart_item.name} - {cart_item.quantity} - {cart_item.price}" for cart_item in self.__shopping_list]
        return [str(item) for item in self.__shopping_list]
    
    def remove_item(self, item_index: int):
        if not 0 <= item_index < len(self.__shopping_list):
            raise IndexError("Index out of range")
        
        self.__shopping_list.pop(item_index)
        
    def calculate_total(self):
        return sum(item.subtotal() for item in self.__shopping_list)
    
    def __len__(self):
        return len(self.__shopping_list)

class CartItem:
    def __init__(self, name, quantity, price):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def __str__(self):
        return f"{self.name} | Qty: {self.quantity} | ${self.price:.2f}"
    
    def subtotal(self):
        return self.price * self.quantity

shoppingcart = ShoppingCart("Iyke's Shopping Lists")

cart_item1 = CartItem("PS5", 1, 3500)
cart_item2 = CartItem("iPhone 17 Pro Max", 4, 1500)
cart_item3 = CartItem("MacBook Pro Max M5 2026", 2, 4500)
cart_item4 = CartItem("iPad M4 Pro 11'", 3, 2500)

shoppingcart.add_cart_item(cart_item1)
shoppingcart.add_cart_item(cart_item2)
shoppingcart.add_cart_item(cart_item3)
shoppingcart.add_cart_item(cart_item4)

print(shoppingcart.name)

shoppingcart.remove_item(2)
# print(shoppingcart.list_cart_items())
# print(f"The sum total of your cart of {len(shoppingcart)} items is: ${shoppingcart.calculate_total():.2f}")

# Create an abstract Employee class with an abstract calculate_salary() method, then implement FullTimeEmployee and PartTimeEmployee.
class Employee(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def calculate_salary(self):
        """Return the employee's salary."""

class FullTimeEmployee(Employee):
    def __init__(self, name: str, monthly_salary: float):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate: float, hours_worked: int):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
employee1 = PartTimeEmployee("Ike", 15, 12)
employee2 = FullTimeEmployee("Chiome", 2500)

print(employee1.calculate_salary())
print(employee2.calculate_salary())

# Polymorphism - employee.calculate_salary() works for every object, even though each class calculates salary differently. That's polymorphism.
employees = [
    FullTimeEmployee("Alice", 5000),
    PartTimeEmployee("Bob", 25, 80),
    FullTimeEmployee("John", 6500)
]

for employee in employees:
    print(
        f"{employee.name}: ${employee.calculate_salary():,.2f}"
    )
