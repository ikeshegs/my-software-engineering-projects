#
class Robot:
    total_robots = 0

    def __init__(self, name):
        self.name = name
        Robot.total_robots += 1

    @classmethod   # The @classmethod tells Python: "This method works with the class, not a particular robot."
    def how_many_robots(cls):   # cls stands for class
        return cls.total_robots
    
r1 = Robot("Bolt")
r2 = Robot("Sparky")

print(Robot.how_many_robots())      # Output: 2

# Another common use: Alternative constructors
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name, int(age))

# person = Person("Alice", 25) # Instead of writing this
person = Person.from_string("Alice,25") # You write this


