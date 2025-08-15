# Introduction to Object-Oriented Programming (OOP) in Python

# OOP is a programming paradigm that uses "objects" to model real-world entities.
# Each object can have:
#   - Attributes (data/variables)
#   - Methods (functions/behaviors)

# Example: Representing a simple 'Car' using a class

class Car:
    # Constructor (initializer) method
    def __init__(self, brand, model, year):
        self.brand = brand      # Attribute: brand of the car
        self.model = model      # Attribute: model of the car
        self.year = year        # Attribute: manufacturing year
    
    # Method to display car details
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"The {self.model}'s engine is now running!")

# Creating objects (instances) of the Car class
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Toyota", "Corolla", 2020)

# Accessing attributes and methods
car1.display_info()
car1.start_engine()

car2.display_info()
car2.start_engine()

"""
Output:
2022 Tesla Model S
The Model S's engine is now running!
2020 Toyota Corolla
The Corolla's engine is now running!
"""

# Key OOP Concepts covered here:
# - Class: Blueprint for creating objects.
# - Object: An instance of a class.
# - Attributes: Data stored in an object.
# - Methods: Functions that define an object's behavior.
# - __init__: Special method to initialize object attributes.
