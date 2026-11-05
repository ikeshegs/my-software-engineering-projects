# Opening a file without using a context manager
file = open("data.txt", "r")

content = file.read()

file.close()

# Opening a file using a context manager
with open("data.txt", "r") as file:
    content = file.read()

# print(content)

# Building your own Context Manager
class MyContext:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):     # This method runs automatically
        """Block of code that runs when the context manager exits."""
        print("Exiting")
        
# with MyContext():
#     print("Inside Block")
    
# Returning a Value - Usually __enter__() returns something
class Database:

    def __enter__(self):
        print("Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnected")

# with Database() as db:
#     print(db)

# Handling Exceptions - The __exit__() method can handle exceptions that occur within the context block
class Example:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleaning up")

with Example():
    print("Working...")
    raise ValueError("Oops!")
