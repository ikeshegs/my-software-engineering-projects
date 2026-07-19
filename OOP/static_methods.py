#
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
Calculator.add(3, 5)

# calc = Calculator()
# calc.add(5, 3) We didn't do this, because the calculator doesn't need to remember anything. It just adds two numbers.

#
class Dog:
    @staticmethod
    def number_of_legs():
        return 4

print(Dog.number_of_legs())     # Output: 4
