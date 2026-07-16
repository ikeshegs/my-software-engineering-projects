# Composition 
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
        
    def start(self) -> str:
        return "Engine vrooms to life!"
    
class Car:
    def __init__(self, brand: str, horsepower: int):
        self.brand = brand
        # Composition: Car instantiates and owns the Engine object
        self.engine = Engine(horsepower)
        
    def start_car(self) -> str:
        # Delegation: Car delegates the start action to its engine component
        return f"{self.brand} is ready. {self.engine.start()}"
    
my_car = Car(brand="Tesla", horsepower=500)
print(my_car.start_car())  # Output: Tesla is ready. Engine vrooms to life!
        
