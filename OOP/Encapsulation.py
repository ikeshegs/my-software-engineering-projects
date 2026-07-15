# Public Attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # Public
        self.balance = balance  # Public

account = BankAccount("Alice", 1000)
account.balance = -5000  # ❌ Bad! External code can easily break the rules.


# Private Attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 🔒 Private attribute
        
    # GETTER: Safe way to read data
    def get_balance(self):
        return self.__balance

    # SETTER: Safe way to change data with strict rules
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("❌ Invalid deposit amount!")

account = BankAccount("Alice", 1000)
# print(account.__balance)  # 💥 Crash! Throws an AttributeError
account.deposit(500)   #  Works: Deposited $500. New balance: $1500
# account.deposit(-50)   # ❌ Prevented: Invalid deposit amount!

# print(account.get_balance())  # Output: 1500

# Using @property Decorator that lets you use getters and setters while still using clean dot notation
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value

item = Product(100)
# print(item.price)  # Output: 100
item.price = 150
# print(item.price)  # Output: 150