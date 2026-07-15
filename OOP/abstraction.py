from abc import ABC, abstractmethod

# This is the Abstract Class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Abstract method; no implementation details here."""
        pass

# Trying to do this will crash:
# my_car = Vehicle() -> TypeError: Can't instantiate abstract class Vehicle

# Enforcing the blueprint (Inheritance)
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Ignition switched on. Engine revving!"

class ElectricCar(Vehicle):
    def start_engine(self):
        return "Power button pressed. Silent hum."

# Instantiating the concrete child classes
bike = Motorcycle()
car = ElectricCar()

print(bike.start_engine())  # Output: Ignition switched on. Engine revving!
print(car.start_engine())   # Output: Power button pressed. Silent hum.

# Combining Concrete and Abstract Methods
class DatabaseConnector(ABC):
    
    # Concrete method: Inherited by all subclasses without rewriting
    def connect(self):
        return "Connecting to server secure portal..."
        
    # Abstract method: Must be uniquely built by each subclass
    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLConnector(DatabaseConnector):
    def execute_query(self, query):
        return f"Running MySQL syntax: {query}"

db = MySQLConnector()
print(db.connect())        # Output: Connecting to server secure portal...
print(db.execute_query("SELECT * FROM users")) # Output: Running MySQL syntax: SELECT * FROM users
