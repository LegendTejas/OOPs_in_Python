#6. Callable Objects
# __call__ method
# Makes an object behave like a function.

class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self, message):
        return f"{self.name} says: {message}"

# Using callable object
greet = Greeter("Alice")
print(greet("Hello, world!"))  # Calls __call__


# Key Points:

# __str__ → Readable string for users

# __repr__ → Debug-friendly representation

# __add__, __sub__, etc. → Arithmetic customization

# __eq__, __lt__, etc. → Comparison customization

# __len__, __getitem__, etc. → Collection-like behavior

# __call__ → Make objects callable like functions
