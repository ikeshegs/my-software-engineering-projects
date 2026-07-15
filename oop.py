# This shows how to create a simple class in Python. The class is named "Person" and it doesn't have any attributes or methods defined. Two instances of the Person class are created, named person1 and person2. When printed, they will show their memory addresses, indicating that they are two distinct objects in memory.
class Person:
    pass

person1 = Person()
person2 = Person()

# print(person1)
# print(person2)

# This shows how to create a class with an __init__ method, which is a special method that is called when an object is created. The __init__ method takes two parameters, name and age, and assigns them to the object's attributes. Two instances of the Person class are created with different names and ages, and their attributes are printed to show that they are unique objects with their own data.
class Person:
    # The __init__ method sets up the initial data
    def __init__(self, name: str, age: int):
        self.name = name    # Assigning arguments to object attributes
        self.age = age

# Creating unique objects (arguments map directly to __init__)
person1 = Person("John", 35)
person2 = Person("Jane", 28)

# print(person1.name, person1.age)
# print(person2.name, person2.age)

# Understanding "self"
class Dog:
    def __init__(self, name: str):
        # self.name belongs to the specific dog being made
        self.name = name 

    def bark(self):
        pass
        # self.name fetches the name of THIS specific dog
        # print(f"{self.name} says woof!")

# Create two distinct objects
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# When you call this:
dog1.bark()  # Output: Buddy says woof!

# Python actually translates it to this behind the scenes:
# Dog.bark(dog1)

# Instance Attribute
class Cat:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

cat1 = Cat("Whiskers", 3)
cat2 = Cat("Luna", 5)

# print(cat1.name)  # Output: Whiskers
# print(cat2.name)  # Output: Luna

# Class Attribute
class Cat:
    # Class attribute (All cats belong to this kingdom)
    kingdom = "Animalia" 

    def __init__(self, name):
        self.name = name

cat1 = Cat("Whiskers")
cat2 = Cat("Luna")

# print(cat1.kingdom)  # Output: Animalia
# print(cat2.kingdom)  # Output: Animalia

# Methods
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed  # Starts at the given speed

    # This is a method
    def accelerate(self, boost):
        self.speed += boost  # Modifies the internal attribute
        # print(f"The {self.color} car accelerated to {self.speed} km/h!")

# Create the object
my_car = Car("Red", 60)

# Call the method using dot notation
my_car.accelerate(20)  # Output: The Red car accelerated to 80 km/h!

# This is side-by-side comparison of Instance, Class, and Static methods inside a single class.
class Pizza:
    # Class attribute shared by ALL pizzas
    total_pizzas_made = 0

    def __init__(self, toppings, size_inches):
        self.toppings = toppings        # Instance attribute
        self.size_inches = size_inches  # Instance attribute
        Pizza.total_pizzas_made += 1    # Increment global counter

    # 1. INSTANCE METHOD
    # Uses 'self' to access specific, unique pizza details.
    def slice_and_serve(self):
        print(f"Cutting your {self.size_inches}-inch {self.toppings} pizza!")

    # 2. CLASS METHOD
    # Uses '@classmethod' and 'cls' to manage global class data.
    @classmethod
    def get_factory_report(cls):
        print(f"Total pizzas baked across all shops: {cls.total_pizzas_made}")

    # 3. STATIC METHOD
    # Uses '@staticmethod'. It is a helper function that needs NO class or object data.
    @staticmethod
    def convert_inches_to_cm(inches):
        return inches * 2.54
    
# Create two unique pizza instances
pizza1 = Pizza("Pepperoni", 12)
pizza2 = Pizza("Margherita", 14)

# --- 1. Testing Instance Method ---
# It only cares about the data inside 'pizza1'
# pizza1.slice_and_serve()  
# Output: Cutting your 12-inch Pepperoni pizza!


# --- 2. Testing Class Method ---
# We call it directly on the Class (Pizza), not the individual objects.
# Pizza.get_factory_report()  
# Output: Total pizzas baked across all shops: 2


# --- 3. Testing Static Method ---
# It doesn't know about pizza1, pizza2, or the counter. It just does math.
cm_size = Pizza.convert_inches_to_cm(12)
# print(f"A 12-inch pizza is {cm_size} cm.")  
# Output: A 12-inch pizza is 30.48 cm.

# Public Attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # Public
        self.balance = balance  # Public

account = BankAccount("Alice", 1000)
account.balance = -5000  # ❌ Bad! External code can easily break the rules.


# Private Attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 🔒 Private attribute
        
    # GETTER: Safe way to read data
    def get_balance(self):
        return self.__balance

    # SETTER: Safe way to change data with strict rules
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("❌ Invalid deposit amount!")

account = BankAccount("Alice", 1000)
# print(account.__balance)  # 💥 Crash! Throws an AttributeError
account.deposit(500)   #  Works: Deposited $500. New balance: $1500
account.deposit(-50)   # ❌ Prevented: Invalid deposit amount!

# print(account.get_balance())  # Output: 1500

# Using @property Decorator that lets you use getters and setters while still using clean dot notation
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value

item = Product(100)
print(item.price)  # Output: 100
item.price = 150
print(item.price)  # Output: 150




