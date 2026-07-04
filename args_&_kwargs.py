#
def my_function(*args):
    return args

print(my_function(5))  # This returns a tuple with a single element (5,)
print(my_function(5, 10, 3)) # This return a tuple with three elements (5, 10 , 3)

# This is an example of *args and **kwargs used together
def example(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    
example(1, 2, 3, name="John", age=30)  # This will print the positional arguments as a tuple and the keyword arguments as a dictionary

# Mixing Normal Parameters, *args, and **kwargs
def greet(greeting, *names, **details):
    print(f"Greetings: {greeting}")
    print(f"Names args: {names}")
    print(f"Details kwargs: {details}")

greet("Hello", "John", "Doe", "Smith", age=30, city="New York")  # This will print the greeting, the names as a tuple, and the details as a dictionary

# Using * to unpack a list into individual arguments
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

print(add(*numbers)) # This will unpack the list into individual arguments and return the sum, which is 60

# Using ** to unpack a dictionary into keyword arguments
def person(name, age):
    print(name)
    print(age)

info = {
    "name": "John",
    "age": 30
}

person(**info) # This will unpack the dictionary into keyword arguments and print the name and age, which are "John" and 30 respectively

