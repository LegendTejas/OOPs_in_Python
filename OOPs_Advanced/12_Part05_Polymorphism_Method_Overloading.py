# Python doesn’t support method overloading like Java/C++.
# But we can simulate it using default parameters or *args.

# Simulated Method Overloading in Python

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(5, 10))       # Two arguments
print(calc.add(5, 10, 15))   # Three arguments
print(calc.add())            # No arguments (defaults to 0)
