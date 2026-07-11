#
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)  # Output: Returns the sum of two numbers.
print(help(add))  # Output: Help on function add in module __main__: add(a, b) -> Returns the sum of two numbers.

# Multi-line docstring
def divide(a, b):
    """
    Divide one number by another.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The quotient.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b

# Single-line docstring
def square(x):
    """Return the square of x."""
    return x ** 2

#

