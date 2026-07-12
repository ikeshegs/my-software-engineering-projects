# This is a simple Python program that prompts the user to enter a number, then attempts to divide 10 by that number. If any error occurs during this process (such as entering a non-integer value or dividing by zero), it will catch the exception and print "Something went wrong!"
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except:
    print("Something went wrong!")
    
# Handling multiple exceptions
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Catching multiple exceptions in a single except block
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")

# The else block is executed if no exceptions are raised in the try block
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
else:
    print("Division successful.")
    
# The finally block is executed regardless of whether an exception was raised or not
try:
    print("Opening a file...")
except:
    print("An error occurred.")
finally:
    print("Closing the file.")

# Using "as" to access the exception object
try:
    number = int(input())
except ValueError as error:
    print(error)
    
# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Creating custom exceptions
class InvalidAgeError(Exception):
    pass

age = -2

if age < 0:
    raise InvalidAgeError("Age cannot be negative.")

# 
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise ValueError("Insufficient funds.")

    return balance - amount


try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amount)

except ValueError as error:
    print("Error:", error)

else:
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

finally:
    print("Thank you for using our ATM.")
