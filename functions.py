# This function demonstrates the use of default parameter values in Python. If no argument is provided for the 'name' parameter, it will default to "Friend".
def greet(name = "Friend"):
    return f"Hello, {name}!"

greet("Alice")
greet() # Using the default value for the name parameter

# Keyword arguments allow you to specify the values of parameters by name, rather than relying on their position in the function call. This can make your code more readable and flexible, especially when dealing with functions that have many parameters or optional parameters.
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."

introduce(age = 45, name = "Bob")  # Using keyword arguments to specify the order of parameters

# This function demonstrates how to return multiple values from a function in Python. The function 'calculate' takes two parameters, 'a' and 'b', and returns both their sum and difference as a tuple. This allows the caller to receive multiple results from a single function call.
def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(10, 5)  # Returns (15, 5) as a tuple containing the sum and difference of a and b

# The two functions below demonstrate how to call one function from within another function. The 'welcome' function calls the 'greet' function to print a greeting message before printing a welcome message. This shows how functions can be composed together to build more complex behavior.
def greet():
    print("Hello")

def welcome():
    greet()
    print("Welcome to the program!") # Calling the greet function from within the welcome function to print a greeting message before the welcome message.
    
square = lambda x: x * x  # This is a lambda function that takes one argument 'x' and returns its square. Lambda functions are anonymous functions defined using the 'lambda' keyword, and they can be used for short, simple operations without the need for a full function definition.

print(square(5))  # Calling the lambda function to calculate the square of 5, which returns 25

print((lambda x, y: x + y)(3, 4))  # This is an example of a lambda function that takes two arguments 'x' and 'y' and returns their sum. It is called immediately with the arguments 3 and 4, returning 7. Python does not encourage using immediately invoked lambda expressions. It simply results from a lambda expression being callable, unlike the body of a normal function.

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# print(full_name('guido', 'van rossum')) # This lambda function takes two arguments, 'first' and 'last', and returns a formatted string representing the full name with proper capitalization. The 'title()' method is used to capitalize the first letter of each name. The function is called with the arguments 'guido' and 'van rossum', returning "Full name: Guido Van Rossum".

# This function demonstrates the use of higher-order functions in Python. A higher-order function is a function that takes another function as an argument or returns a function as its result. In this case, 'high_ord_func' takes two arguments: 'x' and 'func'. It applies the 'func' to 'x' and adds the result to 'x', effectively allowing for dynamic behavior based on the provided function.
high_ord_func = lambda x, func: x + func(x)
# print(high_ord_func(2, lambda x: x * x))  # Returns 6
# print(high_ord_func(2, lambda x: x + 3))  # Returns 7

# Exercise
def square(x):
    return x * x

# print(square(5))  # Calling the square function to calculate the square of 5, which returns 25

def is_even(number):
    if number % 2 == 0:
        return True
    return False

# print(is_even(3))
# print(is_even(10))

def is_positive(number):
    # return isinstance(number, (int, float)) and number > 0
    return number > 0

# print(is_positive(-5))
# print(is_positive(5))

def max_value(a, b, c):
    return max(a, b, c)

# print(max_value(10, 20, 15))  # Calling the max_value function to find the maximum value among 10, 20, and 15, which returns 20
# print(max_value(-5, -10, -3))  # Calling the max_value function to find the maximum value among -5, -10, and -3, which returns -3

def number_vowels_in_string(name):
    name = name.lower()
    count = 0
    
    for char in name:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
    return count

# print(number_vowels_in_string("Hello"))  # Calling the number_vowels_in_string function to count the number of vowels in the string "Hello", which returns 2

def fac(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if x == 0 or x == 1:
        return 1
    else:
        return x * fac(x - 1)

print(fac(5))

def reverse_string(name):
    return name[::-1]

print(reverse_string("Hello"))  # Calling the reverse_string function to reverse the string "Hello", which returns "olleH"

def avr_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    return sum(numbers) / len(numbers)

print(avr_value([1, 2, 3, 4, 5]))  # Calling the avr_value function to calculate the average of the list [1, 2, 3, 4, 5], which returns 3.0

def is_palindrome(name):
    if name == name[::-1]:
        return "This word is a Palindrome"
    return "This word is not a Palindrome"

print(is_palindrome("world"))
print(is_palindrome("racecar"))
