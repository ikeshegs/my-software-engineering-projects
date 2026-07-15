# Polymorphism
# Duck Typing ("Polymorphism without Inheritance")
class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep boop!"

# This function doesn't care about the class hierarchy.
# It only cares that the object passed has a 'speak' method.
def activate_voice(speaker):
    print(speaker.speak())

activate_voice(Dog())    # Output: Woof!
activate_voice(Robot())  # Output: Beep boop!

# Polymorphism - Method Overriding
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Iterate through different objects using the same method name
# All objects respond to speak() differently based on their class.
animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())   # Output: Woof!, Meow!