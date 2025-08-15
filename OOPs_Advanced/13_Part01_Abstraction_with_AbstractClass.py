# Abstraction in Python
# Abstraction means showing only essential details and hiding the background implementation.
# In Python, we use the 'abc' module to create Abstract Classes and Methods.

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method - must be implemented in subclass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete Class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key.")

    def stop_engine(self):
        print("Car engine stopped.")

class ElectricScooter(Vehicle):
    def start_engine(self):
        print("Electric scooter started silently.")

    def stop_engine(self):
        print("Electric scooter stopped.")

# Creating objects
car = Car()
scooter = ElectricScooter()

car.start_engine()
car.stop_engine()

scooter.start_engine()
scooter.stop_engine()
