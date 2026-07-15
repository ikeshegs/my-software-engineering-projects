# Inheritance in OOP
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Child Class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

# Usage
my_dog = Dog("Buddy")
# print(my_dog.eat())  # Inherited method -> "Buddy is eating."
# print(my_dog.bark()) # Child-specific method -> "Buddy says Woof!"

# Using the super() function. The super() is used to preserve the parents __init__() method.
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name) # Calls Parent's __init__
        self.can_fly = can_fly  # New child attribute

# Method Overriding. The child class can override a parent method, when you want to implement a specific implementation for the child class.
class Cat(Animal):
    def eat(self):
        return f"{self.name} picks at their food politely." 
        # Completely overrides Animal.eat()
        
# Multiple Inheritance Example
class Engine:
    def start_engine(self):
        return "Engine rumbling."

class Machine:
    def power_on(self):
        return "System online."

# Inherits from BOTH classes
class Car(Engine, Machine):
    pass

my_car = Car()
# print(my_car.start_engine()) 
# print(my_car.power_on())

# Method Resolution Order (MRO)
# print(Car.mro())