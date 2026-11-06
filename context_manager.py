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

# with Example():
#     print("Working...")
#     raise ValueError("Oops!")

# Using a generator to create a Context Manager
from contextlib import contextmanager
import time

@contextmanager
def managed_timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"Elapsed time: {end - start:.4f} seconds")
        
# with managed_timer():
#     total = sum(range(10_000_000))
    
# Creating a Context Manager class that prints messages when entering and exiting the context
class MyContextManager:
    def __enter__(self):
        print("Entering...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting...")

# with MyContextManager():
#     print("Inside the context manager.")
    
# Build a context manager that measures how long a block of code takes to execute
class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds")
        
# with Timer() as timer:
#     total = sum(range(10_000))
    
# Create a context manager that writes logs to a file when entering and exiting the context
class Logger:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, "a")
        self.file.write("\n")
        self.file.write("Task started\n")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.write("Task ended\n")
        self.file.close()
        
with Logger("log.txt") as logger:
    logger.file.write("Performing some task...\n")
    logger.file.write("Task completion in progress\n")
    logger.file.write("Task completed successfully.\n")


