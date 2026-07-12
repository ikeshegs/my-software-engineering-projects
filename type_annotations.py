from typing import Any, Callable

# This is a simple function that takes a string argument `name` and returns a greeting message. The function uses type annotations to specify that the input `name` should be of type `str` and the return value will also be of type `str`.
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Type annotation for a list of integers. This Specifies the type of elements inside collections.
numbers: list[int] = [1, 2, 3]

def total(nums: list[int]) -> int:
    return sum(nums)

# Type annotation for a dictionary with string keys and integer values.
student: dict[str, int] = {
    """
    keys are strings 
    values are integers
    """
    
    "Math": 90,
    "Science": 85
}

# Optional return type: The function `find_user` takes an integer `id` as input and returns either a string (the user's name) or None if the user is not found. The return type is specified as `str | None`, indicating that the function can return either a string or None.
def find_user(id: int) -> str | None:
    pass

# Union type annotation: The function `double` takes a value that can be either an integer or a float and returns a float. The input type is specified as `int | float`, indicating that the function can accept either type, and the return type is specified as `float`.
def double(value: int | float) -> float:
    return value * 2

# Any type annotation: The function `process` takes an argument of any type and prints it. This is useful when the type of the argument is not known or can be of multiple types.
def process(data: Any):
    print(data)

# Annotation for a function with multiple parameters: The function `introduce` takes three parameters: `name` (a string), `age` (an integer), and `employed` (a boolean). The return type is specified as `str`, indicating that the function will return a string.
def introduce(name: str, age: int, employed: bool) -> str:
    return f"{name} is {age} years old."

# Default values
def greet(name: str = "Guest") -> str:
    return f"Hello {name}"

# Annotating Lambda Functions. This is a lambda function that takes two integers and returns their sum. The type annotation specifies that the function takes two integers as input and returns an integer.
add: Callable[[int, int], int] = lambda x, y: x + y

# This function takes a callable (a function) as an argument, along with two integers. It calls the provided function with the two integers and returns the result. The type annotation specifies that `func` is a callable that takes two integers and returns an integer, and the return type of `operate` is also an integer.
def operate(
    func: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return func(a, b)

# Type Aliases: This is a type alias that defines `Scores` as a dictionary where the keys are strings and the values are lists of integers. This can be useful for improving code readability and maintainability.
type Scores = dict[str, list[int]]

student_scores: Scores = {
    "Alice": [90, 80],
    "Bob": [70, 95]
}

# Function to apply a discount to a price.
def apply_discount(price: float, discount: float) -> float:
    """Applies a discount to a given price."""
    return price * (1 - discount)

def process_prices(
    prices: list[float],
    operation: Callable[[float, float], float],
    discount: float
) -> list[float]:
    """
    Processes a list of prices using a specified operation and discount.
    
    Args:
        prices: A list of prices to be processed.
        operation: A callable that takes a price and a discount and returns the processed price.
        discount: The discount to be applied to each price.
        
    Returns:
        A list of the processed prices.
    """
    return [operation(price, discount) for price in prices]

prices = [100.0, 200.0, 300.0]

new_prices = process_prices(
    prices,
    apply_discount,
    0.2
)

print(new_prices)
