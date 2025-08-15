# Encapsulation in Python
# Encapsulation is the concept of restricting direct access to some variables and methods.
# In Python, it is implemented using:
#   Public Members    → Accessible from anywhere
#   Protected Members → Accessible within class and subclasses (_single_underscore)
#   Private Members   → Accessible only within the class (__double_underscore)

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder        # Public attribute
        self._account_type = "Savings"              # Protected attribute
        self.__balance = balance                    # Private attribute

    # Public method
    def show_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self._account_type}")
        print(f"Balance: {self.__balance}")

    # Public method to access private data safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Public method to access private data safely
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount!")

# Creating object
account = BankAccount("Alice", 1000)

# Accessing public method
account.show_account_info()

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(300)

# Trying to access private attribute directly (will fail)
# print(account.__balance)  # AttributeError

# Accessing protected attribute (possible, but discouraged)
print(f"Protected attribute access: {account._account_type}")

# Accessing private attribute using name mangling (not recommended)
print(f"Private attribute access via name mangling: {account._BankAccount__balance}")

"""
Output:
Account Holder: Alice
Account Type: Savings
Balance: 1000
Deposited: 500. New Balance: 1500
Withdrawn: 300. New Balance: 1200
Protected attribute access: Savings
Private attribute access via name mangling: 1200
"""

# Key points:
# - Public: Accessible everywhere.
# - Protected (_var): Accessible within class & subclasses, not enforced strictly.
# - Private (__var): Name-mangled to prevent direct access.
# - Always use getter/setter methods to access private data safely.
