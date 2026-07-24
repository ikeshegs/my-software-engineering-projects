import time

from functools import wraps

def my_decorator(func):

    def wrapper():
        print("Starting...")
        func()
        print("Finished!")

    return wrapper

@my_decorator
def greet():
    print("Hello")

# greet()

# Functions with arguments
def decorator(func):
    
    def wrapper(name):
        print("It's about to begin....")
        func(name)
        print("It's done....")
        
    return wrapper

@decorator
def greet2(name):
    print(f"Hello, {name}")
    
# greet2("Ikechukwu")

# Acceping any number of arguments
def second_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Before...")
        result = func(*args, **kwargs)
        print("After...")
        
        return result
    
    return wrapper

@second_decorator
def add(a, b):
    return a + b

# print(add(8, 9))

# Preserving Function Metadata
# A custom decorator can hide the original function's name and docstring. Use functools.wraps to preserve them.
def decorator3(func):

    @wraps(func)                        # <--- Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@decorator3
def addd(a, b, c):
    return a + b + c

# print(addd(18, 34, 91))

# PRACTICE!!!!
def announce(func):
    
    def wrapper():
        print("Calling function...")
        func()
        print("Function finished!")
    
    return wrapper

@announce
def say_hi():
    print("Hi!")

# say_hi()

# Stacking Mulitiple Decorators
def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator One - Before")
        result = func(*args, **kwargs)
        print("Decorator One - After")
        return result
    return wrapper


def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator Two - Before")
        result = func(*args, **kwargs)
        print("Decorator Two - After")
        return result
    return wrapper

@decorator_one
@decorator_two
def greet3():
    print("Hello!")
    
# greet3()

# Example: Authentication + Logging
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Checking login...")
        return func(*args, **kwargs)
    return wrapper

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Logging request...")
        return func(*args, **kwargs)
    return wrapper

@login_required
@log_activity
def dashboard():
    print("Dashboard opened.")

# dashboard()

# Example: Timing + Logging
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Took {end - start:.4f} seconds")
        return result
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
@timer
def calculate():
    total = sum(range(1_000_000))
    return total

# calculate()

# 
def A(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("A Before...")
        result = func(*args, **kwargs)
        print("A After...")
        return result
    return wrapper

def B(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("B Before...")
        result = func(*args, **kwargs)
        print("B After...")
        return result
    return wrapper
    
def C(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("C Before...")
        result = func(*args, **kwargs)
        print("C After...")
        return result
    return wrapper
    
def hello():
    print("Hello")
    
hello = A(B(C(hello)))

# hello()

# CLASS DECORATORS
def add_country(cls):
    cls.country = "Nigeria"
    return cls

@add_country
class Person:
    pass

p = Person()

# print(p.country)

# Decorators can also add methods.
def add_greeting(cls):

    def greet(self):
        print(f"Hello, I'm {self.name}")

    cls.greet = greet
    return cls

@add_greeting
class Person:

    def __init__(self, name):
        self.name = name
        
p = Person("Iyke")
# p.greet()

# Modifying Existing Methods
def loud(cls):

    original = cls.speak

    @wraps(original)
    def new_speak(self):
        print("VERY LOUD:")
        original(self)

    cls.speak = new_speak
    return cls

@loud
class Dog:

    def speak(self):
        print("Woof!")

# Dog().speak()

# Examples of class decorators

# Registering Plugins
plugins = []

def register(cls):
    plugins.append(cls)
    return cls

@register
class PDFExporter:
    pass

@register
class CSVExporter:
    pass

# print(plugins)

# Logging Class Creation
def log_class(cls):
    # print(f"Creating class {cls.__name__}")
    return cls

@log_class
class Employee:
    pass

# Decorators Can Return a Different Class
def replace(cls):

    class NewClass(cls):

        def hello(self):
            print("Hello!")

    return NewClass

@replace
class Person:
    pass

p = Person()
p.hello()




