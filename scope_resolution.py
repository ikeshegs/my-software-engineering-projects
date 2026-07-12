# Local Scope
# A local scope contains variables defined inside a function. These variables only exist while the function is running.
def greet():
    message = "Hello"
    print(message)

greet()

# Enclosing Scope
# An enclosing scope exists when one function is defined inside another (nested functions).
def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    inner()

outer()

# Modifying an Enclosing Variable
# Use the "nonlocal" keyword.
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()
    print(count)

outer()

# Global Scope
# A global scope contains variables defined at the top level of a script or module. These variables can be accessed from any function within the same module.
language = "Python"

def show_language():
    print(language)

show_language()

# Modifying a Global Variable
# Use the "global" keyword.
count = 0

def increment():
    global count
    count += 1

increment()

print(count)

# Built-in Scope
# The built-in scope contains names that are pre-defined in Python. These names are available in any part of the code, including functions and classes.
def show_builtin():
    print(len("Hello"))
